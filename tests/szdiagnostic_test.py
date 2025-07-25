#! /usr/bin/env python3


import json

import pytest
from pytest_schema import schema
from senzing import SzDiagnostic, SzEngine, SzError, SzSdkError

from senzing_grpc import SzDiagnosticGrpc, SzEngineGrpc

from .helpers import get_grpc_channel

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_check_repository_performance(sz_diagnostic: SzDiagnostic) -> None:
    """Test SzDiagnostic.check_repository_performance()."""
    seconds_to_run = 3
    actual = sz_diagnostic.check_repository_performance(seconds_to_run)
    actual_as_dict = json.loads(actual)
    assert schema(check_repository_performance_schema) == actual_as_dict


def test_check_repository_performance_bad_seconds_to_run_type(
    sz_diagnostic: SzDiagnostic,
) -> None:
    """Test SzDiagnostic.check_repository_performance()."""
    bad_seconds_to_run = "string"
    with pytest.raises(SzSdkError):
        sz_diagnostic.check_repository_performance(bad_seconds_to_run)  # type: ignore[arg-type]


def test_check_repository_performance_bad_seconds_to_run_value(
    sz_diagnostic: SzDiagnostic,
) -> None:
    """Test SzDiagnostic.check_repository_performance()."""
    bad_seconds_to_run = -1
    # with pytest.raises(SzDatabaseError):
    #     sz_diagnostic.check_repository_performance(bad_seconds_to_run)
    actual = sz_diagnostic.check_repository_performance(bad_seconds_to_run)
    actual_as_dict = json.loads(actual)
    assert schema(check_repository_performance_schema) == actual_as_dict


def test_get_repository_info(sz_diagnostic: SzDiagnostic) -> None:
    """Test SzDiagnostic.get_repository_info()."""
    actual = sz_diagnostic.get_repository_info()
    actual_as_dict = json.loads(actual)
    assert schema(get_repository_info_schema) == actual_as_dict


def test_get_feature(sz_diagnostic: SzDiagnostic, sz_engine: SzEngine) -> None:
    """Test SzDiagnostic.get_feature()."""
    data_source_code = "TEST"
    record_id = "1"
    record_definition: str = '{"NAME_FULL": "Joe Blogs", "DATE_OF_BIRTH": "07/07/1976"}'
    sz_engine.add_record(data_source_code, record_id, record_definition)
    actual = sz_diagnostic.get_feature(1)
    actual_as_dict = json.loads(actual)
    assert schema(get_feature_schema) == actual_as_dict


def test_get_feature_unknown_id(sz_diagnostic: SzDiagnostic) -> None:
    """Test SzDiagnostic.get_feature()."""
    with pytest.raises(SzError):
        _ = sz_diagnostic.get_feature(111111111111111111)


def test_help_1(sz_diagnostic: SzDiagnostic) -> None:
    """Test SzDiagnostic.help()."""
    sz_diagnostic.help()


def test_help_2(sz_diagnostic: SzDiagnostic) -> None:
    """Test SzDiagnostic.help(...)."""
    sz_diagnostic.help("check_repository_performance")


# -----------------------------------------------------------------------------
# Unique testcases
# -----------------------------------------------------------------------------


def test_constructor() -> None:
    """Test constructor."""
    actual = SzDiagnosticGrpc(grpc_channel=get_grpc_channel())
    assert isinstance(actual, SzDiagnostic)


def test_context_management() -> None:
    """Test the use of SzDiagnostic in context."""
    with SzDiagnosticGrpc(grpc_channel=get_grpc_channel()) as sz_diagnostic:
        actual = sz_diagnostic.get_repository_info()
        actual_json = json.loads(actual)
        assert schema(get_repository_info_schema) == actual_json


# -----------------------------------------------------------------------------
# Fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_diagnostic", scope="function")
def szdiagnostic_fixture() -> SzDiagnostic:
    """
    SzDiagnostic object to use for all tests.
    """
    result = SzDiagnosticGrpc(grpc_channel=get_grpc_channel())
    return result


@pytest.fixture(name="sz_engine", scope="function")
def szengine_fixture() -> SzEngine:
    """
    SzEngine object to use for all tests.
    """
    result = SzEngineGrpc(grpc_channel=get_grpc_channel())
    return result


# -----------------------------------------------------------------------------
# Schemas
# -----------------------------------------------------------------------------

check_repository_performance_schema = {"numRecordsInserted": int, "insertTime": int}

get_repository_info_schema = {
    "dataStores": [
        {
            "id": str,
            "type": str,
            "location": str,
        }
    ],
}

get_feature_schema = {"LIB_FEAT_ID": int, "FTYPE_CODE": str, "ELEMENTS": [{str: str}]}
