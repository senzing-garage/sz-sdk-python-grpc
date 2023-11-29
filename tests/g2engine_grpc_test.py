import json

import grpc
import pytest
from pytest_schema import schema

from senzing import g2engine_grpc

# -----------------------------------------------------------------------------
# G2Engine fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="g2_engine", scope="module")
def g2engine_fixture():
    """
    Single engine object to use for all tests.
    """

    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    result = g2engine_grpc.G2EngineGrpc(grpc_channel=grpc_channel)
    return result


# -----------------------------------------------------------------------------
# G2Engine schemas
# -----------------------------------------------------------------------------

add_record_with_info_schema = {
    "DATA_SOURCE": str,
    "RECORD_ID": str,
    "AFFECTED_ENTITIES": [],
    "INTERESTING_ENTITIES": {"ENTITIES": []},
}

# -----------------------------------------------------------------------------
# G2Engine testcases
# -----------------------------------------------------------------------------


def test_constructor():
    """Test constructor."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    actual = g2engine_grpc.G2EngineGrpc(grpc_channel=grpc_channel)
    assert isinstance(actual, g2engine_grpc.G2EngineGrpc)


def test_add_record(g2_engine):
    """Test G2Engine().add_record()."""
    data_source_code = "TEST"
    record_id = "1"
    json_data = {}
    load_id = "Test Load"
    g2_engine.add_record(data_source_code, record_id, json_data, load_id)


def test_add_record_with_info(g2_engine):
    """Test G2Engine().add_record()."""
    data_source_code = "TEST"
    record_id = "1"
    json_data = {}
    load_id = "Test Load"
    actual = g2_engine.add_record_with_info(
        data_source_code, record_id, json_data, load_id
    )
    actual_json = json.loads(actual)
    assert schema(add_record_with_info_schema) == actual_json
