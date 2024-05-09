import json
from typing import Dict

import grpc
import pytest
from pytest_schema import schema

from senzing_grpc import SzDiagnostic, SzEngineFlags

# -----------------------------------------------------------------------------
# SzDiagnostic testcases
# -----------------------------------------------------------------------------


def test_constructor() -> None:
    """Test constructor."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    actual = SzDiagnostic(grpc_channel=grpc_channel)
    assert isinstance(actual, SzDiagnostic)


def test_check_datastore_performance(sz_diagnostic: SzDiagnostic) -> None:
    """Test SzDiagnostic().check_datastore_performance()."""
    seconds_to_run = 3
    actual = sz_diagnostic.check_datastore_performance(seconds_to_run)
    actual_as_dict = json.loads(actual)
    assert schema(check_datastore_performance_schema) == actual_as_dict


def test_check_datastore_performance_bad_seconds_to_run_type(
    sz_diagnostic: SzDiagnostic,
) -> None:
    """Test SzDiagnostic().check_datastore_performance()."""
    bad_seconds_to_run = "string"
    with pytest.raises(TypeError):
        sz_diagnostic.check_datastore_performance(bad_seconds_to_run)  # type: ignore[arg-type]


def test_check_datastore_performance_bad_seconds_to_run_value(
    sz_diagnostic: SzDiagnostic,
) -> None:
    """Test SzDiagnostic().check_datastore_performance()."""
    bad_seconds_to_run = -1
    sz_diagnostic.check_datastore_performance(bad_seconds_to_run)


def test_get_datastore_info(sz_diagnostic: SzDiagnostic) -> None:
    """Test SzDiagnostic().get_datastore_info()."""
    actual = sz_diagnostic.get_datastore_info()
    actual_as_dict = json.loads(actual)
    assert schema(get_datastore_info_schema) == actual_as_dict


def test_initialize_and_destroy(sz_diagnostic: SzDiagnostic) -> None:
    """Test SzDiagnostic().init() and SzDiagnostic.destroy()."""
    instance_name = "Example"
    settings: Dict[str, str] = {}
    verbose_logging = SzEngineFlags.SZ_NO_LOGGING
    sz_diagnostic.initialize(instance_name, settings, verbose_logging)
    sz_diagnostic.destroy()


def test_context_managment() -> None:
    """Test the use of SzDiagnostic in context."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    with SzDiagnostic(grpc_channel=grpc_channel) as sz_diagnostic:
        actual = sz_diagnostic.get_datastore_info()
        actual_json = json.loads(actual)
        assert schema(get_datastore_info_schema) == actual_json


# -----------------------------------------------------------------------------
# SzDiagnostic fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_diagnostic", scope="module")  # type: ignore[misc]
def szdiagnostic_fixture() -> SzDiagnostic:
    """
    Single engine object to use for all tests.
    """

    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    result = SzDiagnostic(grpc_channel=grpc_channel)
    return result


# -----------------------------------------------------------------------------
# SzDiagnostic schemas
# -----------------------------------------------------------------------------


get_datastore_info_schema = {
    "dataStores": [
        {
            "id": str,
            "type": str,
            "location": str,
        }
    ],
}

check_datastore_performance_schema = {"numRecordsInserted": int, "insertTime": int}
