import json

import grpc
import pytest
from pytest_schema import schema

from senzing_grpc import SzEngineFlags, szdiagnostic_grpc

# -----------------------------------------------------------------------------
# SzDiagnostic testcases
# -----------------------------------------------------------------------------


def test_constructor() -> None:
    """Test constructor."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    actual = szdiagnostic_grpc.SzDiagnosticGrpc(grpc_channel=grpc_channel)
    assert isinstance(actual, szdiagnostic_grpc.SzDiagnosticGrpc)


def test_check_datastore_performance(
    sz_diagnostic: szdiagnostic_grpc.SzDiagnosticGrpc,
) -> None:
    """Test SzDiagnostic().check_datastore_performance()."""
    seconds_to_run = 3
    actual = sz_diagnostic.check_datastore_performance(seconds_to_run)

    print(">>>> 1:", actual)

    actual_json = json.loads(actual)
    assert schema(check_datastore_performance_schema) == actual_json


def test_check_datastore_performance_bad_seconds_to_run_type(
    sz_diagnostic: szdiagnostic_grpc.SzDiagnosticGrpc,
) -> None:
    """Test SzDiagnostic().check_datastore_performance()."""
    bad_seconds_to_run = "string"
    with pytest.raises(TypeError):
        sz_diagnostic.check_datastore_performance(bad_seconds_to_run)  # type: ignore[arg-type]


def test_check_datastore_performance_bad_seconds_to_run_value(
    sz_diagnostic: szdiagnostic_grpc.SzDiagnosticGrpc,
) -> None:
    """Test SzDiagnostic().check_datastore_performance()."""
    bad_seconds_to_run = -1
    sz_diagnostic.check_datastore_performance(bad_seconds_to_run)


def test_get_datastore_info(sz_diagnostic: szdiagnostic_grpc.SzDiagnosticGrpc) -> None:
    """Test SzDiagnostic().get_datastore_info()."""
    actual = sz_diagnostic.get_datastore_info()

    print(">>>> 2:", actual)

    actual_json = json.loads(actual)
    assert schema(get_datastore_info_schema) == actual_json


def test_initialize_and_destroy(
    sz_diagnostic: szdiagnostic_grpc.SzDiagnosticGrpc,
) -> None:
    """Test SzDiagnostic().init() and SzDiagnostic.destroy()."""
    instance_name = "Example"
    settings = {}
    verbose_logging = SzEngineFlags.SZ_NO_LOGGING
    sz_diagnostic.initialize(instance_name, settings, verbose_logging)
    sz_diagnostic.destroy()


def test_context_managment() -> None:
    """Test the use of SzDiagnosticGrpc in context."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    with szdiagnostic_grpc.SzDiagnosticGrpc(grpc_channel=grpc_channel) as sz_diagnostic:
        actual = sz_diagnostic.get_datastore_info()

        print(">>>> 3:", actual)

        actual_json = json.loads(actual)
        assert schema(get_datastore_info_schema) == actual_json


# -----------------------------------------------------------------------------
# SzDiagnostic fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_diagnostic", scope="module")  # type: ignore[misc]
def szdiagnostic_fixture() -> szdiagnostic_grpc.SzDiagnosticGrpc:
    """
    Single engine object to use for all tests.
    """

    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    result = szdiagnostic_grpc.SzDiagnosticGrpc(grpc_channel=grpc_channel)
    return result


# -----------------------------------------------------------------------------
# SzDiagnostic schemas
# -----------------------------------------------------------------------------


get_datastore_info_schema = {
    "Hybrid Mode": bool,
    "Database Details": [
        {
            "Name": str,
            "Type": str,
        }
    ],
}

check_datastore_performance_schema = {"numRecordsInserted": int, "insertTime": int}
