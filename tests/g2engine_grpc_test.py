import json

import grpc
import pytest
from pytest_schema import schema
from testdata.truthset.customers import TRUTHSET_CUSTOMER_RECORDS
from testdata.truthset.datasources import TRUTHSET_DATASOURCES

from senzing import g2config_grpc, g2configmgr_grpc, g2engine_grpc, g2exception

# -----------------------------------------------------------------------------
# G2Engine fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="g2_config", scope="module")
def g2config_fixture():
    """
    Single engine object to use for all tests.
    """

    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    result = g2config_grpc.G2ConfigGrpc(grpc_channel=grpc_channel)
    return result


@pytest.fixture(name="g2_configmgr", scope="module")
def g2configmgr_fixture():
    """
    Single engine object to use for all tests.
    """

    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    result = g2configmgr_grpc.G2ConfigMgrGrpc(grpc_channel=grpc_channel)
    return result


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

export_json_entity_report_iteritems_schema = {
    "RESOLVED_ENTITY": {
        "ENTITY_ID": int,
        "ENTITY_NAME": str,
        "FEATURES": {},
        "RECORDS": [
            {
                "DATA_SOURCE": str,
                "RECORD_ID": str,
                "ENTITY_TYPE": str,
                "INTERNAL_ID": int,
                "ENTITY_KEY": str,
                "ENTITY_DESC": str,
                "MATCH_KEY": str,
                "MATCH_LEVEL": int,
                "MATCH_LEVEL_CODE": str,
                "ERRULE_CODE": str,
                "LAST_SEEN_DT": str,
            }
        ],
    },
    "RELATED_ENTITIES": [],
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


def test_add_record_bad_data_source_code_type(g2_engine):
    """Test G2Engine().add_record()."""
    data_source_code = 1
    record_id = "1"
    json_data = {}
    load_id = "Test Load"
    with pytest.raises(TypeError):
        g2_engine.add_record(data_source_code, record_id, json_data, load_id)


def test_add_record_bad_data_source_code_value(g2_engine):
    """Test G2Engine().add_record()."""
    data_source_code = "DOESN'T EXIST"
    record_id = "1"
    json_data = {}
    load_id = "Test Load"
    with pytest.raises(g2exception.G2UnknownDatasourceError):
        g2_engine.add_record(data_source_code, record_id, json_data, load_id)


def test_add_record_with_info(g2_engine):
    """Test G2Engine().add_record_with_info()."""
    data_source_code = "TEST"
    record_id = "1"
    json_data = {}
    load_id = "Test Load"
    actual = g2_engine.add_record_with_info(
        data_source_code, record_id, json_data, load_id
    )
    actual_json = json.loads(actual)
    assert schema(add_record_with_info_schema) == actual_json


def test_add_record_with_info_bad_data_source_code_type(g2_engine):
    """Test G2Engine().add_record_with_info()."""
    data_source_code = 1
    record_id = "1"
    json_data = {}
    load_id = "Test Load"
    with pytest.raises(TypeError):
        _ = g2_engine.add_record_with_info(
            data_source_code, record_id, json_data, load_id
        )


def test_add_record_with_info_bad_data_source_code_value(g2_engine):
    """Test G2Engine().add_record_with_info()."""
    data_source_code = "DOESN'T EXIST"
    record_id = "1"
    json_data = {}
    load_id = "Test Load"
    with pytest.raises(g2exception.G2UnknownDatasourceError):
        _ = g2_engine.add_record_with_info(
            data_source_code, record_id, json_data, load_id
        )


def test_export_json_entity_report_iteritems(g2_engine, g2_configmgr, g2_config):
    """Test G2Engine().add_record()."""

    # Add data sources.

    config_handle = g2_config.create()
    for _, value in TRUTHSET_DATASOURCES.items():
        g2_config.add_data_source(config_handle, value.get("Json", ""))
    json_config = g2_config.save(config_handle)
    new_config_id = g2_configmgr.add_config(json_config, "Test")
    g2_configmgr.set_default_config_id(new_config_id)
    g2_engine.reinit(new_config_id)

    # Add records.

    customer_ids = ["1001", "1002", "1003"]
    load_id = "Test Load"
    for customer_id in customer_ids:
        customer = TRUTHSET_CUSTOMER_RECORDS.get(customer_id, {})
        g2_engine.add_record(
            customer.get("DataSource"),
            customer.get("Id"),
            customer.get("Json"),
            load_id,
        )

    # Test export.

    i = 0
    for actual in g2_engine.export_json_entity_report_iteritems():
        i += 1
        actual_json = json.loads(actual)
        assert schema(export_json_entity_report_iteritems_schema) == actual_json
    assert i == 2


def test_context_managment():
    """Test the use of G2EngineGrpc in context."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    with g2engine_grpc.G2EngineGrpc(grpc_channel=grpc_channel) as g2_engine:
        data_source_code = "TEST"
        record_id = "2"
        json_data = "{}"
        load_id = "Test Load"
        g2_engine.add_record(data_source_code, record_id, json_data, load_id)
