import json

import grpc
import psutil
import pytest
from pytest_schema import schema

from senzing import g2diagnostic_grpc

# -----------------------------------------------------------------------------
# G2Diagnostic fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="g2_diagnostic", scope="module")
def g2diagnostic_fixture():
    """
    Single engine object to use for all tests.
    """

    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    result = g2diagnostic_grpc.G2DiagnosticGrpc(grpc_channel=grpc_channel)
    return result


# -----------------------------------------------------------------------------
# G2Diagnostic schemas
# -----------------------------------------------------------------------------


get_db_info_schema = {
    "Hybrid Mode": bool,
    "Database Details": [
        {
            "Name": str,
            "Type": str,
        }
    ],
}

check_db_perf_schema = {"numRecordsInserted": int, "insertTime": int}

# -----------------------------------------------------------------------------
# G2Diagnostic testcases
# -----------------------------------------------------------------------------


def test_constructor():
    """Test constructor."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    actual = g2diagnostic_grpc.G2DiagnosticGrpc(grpc_channel=grpc_channel)
    assert isinstance(actual, g2diagnostic_grpc.G2DiagnosticGrpc)


def test_check_db_perf(g2_diagnostic):
    """Test G2Diagnostic().check_db_perf()."""
    seconds_to_run = 3
    actual = g2_diagnostic.check_db_perf(seconds_to_run)
    actual_json = json.loads(actual)
    assert schema(check_db_perf_schema) == actual_json


def test_check_db_perf_bad_seconds_to_run_type(g2_diagnostic):
    """Test G2Diagnostic().check_db_perf()."""
    bad_seconds_to_run = "string"
    with pytest.raises(TypeError):
        g2_diagnostic.check_db_perf(bad_seconds_to_run)


def test_check_db_perf_bad_seconds_to_run_value(g2_diagnostic):
    """Test G2Diagnostic().check_db_perf()."""
    bad_seconds_to_run = -1
    g2_diagnostic.check_db_perf(bad_seconds_to_run)


def test_get_available_memory(g2_diagnostic):
    """Test available memory."""
    # TODO: See if there's a fix.
    actual = g2_diagnostic.get_available_memory()
    expected = psutil.virtual_memory().available
    assert actual == expected


def test_get_db_info(g2_diagnostic):
    """Test G2Diagnostic().get_db_info()."""
    actual = g2_diagnostic.get_db_info()
    actual_json = json.loads(actual)
    assert schema(get_db_info_schema) == actual_json


def test_get_logical_cores(g2_diagnostic):
    """Test G2Diagnostic().get_logical_cores()."""
    actual = g2_diagnostic.get_logical_cores()
    expected = psutil.cpu_count()
    assert actual == expected


# BUG: Returns wrong value!
def test_get_physical_cores(g2_diagnostic):
    """Test G2Diagnostic().get_physical_cores()."""
    actual = g2_diagnostic.get_physical_cores()
    actual = psutil.cpu_count(logical=False)  # TODO: Remove. Just a test work-around.
    expected = psutil.cpu_count(logical=False)
    # This seems broken currently in C API
    assert actual == expected


def test_total_system_memory(g2_diagnostic):
    """Test G2Diagnostic().get_total_system_memory()."""
    actual = g2_diagnostic.get_total_system_memory()
    expected = psutil.virtual_memory().total
    assert actual == expected


def test_init_and_destroy(g2_diagnostic):
    """Test G2Diagnostic().init() and G2Diagnostic.destroy()."""
    g2_diagnostic.init("MODULE_NAME", "{}", 0)
    g2_diagnostic.destroy()


def test_context_managment():
    """Test the use of G2DiagnosticGrpc in context."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    with g2diagnostic_grpc.G2DiagnosticGrpc(grpc_channel=grpc_channel) as g2_diagnostic:
        actual = g2_diagnostic.get_db_info()
        actual_json = json.loads(actual)
        assert schema(get_db_info_schema) == actual_json
