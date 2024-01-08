import json
from typing import Any, Dict

import grpc
import pytest
from pytest_schema import Or, schema
from testdata.truthset.customers import TRUTHSET_CUSTOMER_RECORDS
from testdata.truthset.datasources import TRUTHSET_DATASOURCES
from testdata.truthset.references import TRUTHSET_REFERENCE_RECORDS
from testdata.truthset.watchlist import TRUTHSET_WATCHLIST_RECORDS

from senzing_grpc import (
    G2UnknownDatasourceError,
    g2config_grpc,
    g2configmgr_grpc,
    g2engine_grpc,
)

# -----------------------------------------------------------------------------
# G2Engine fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="g2_config", scope="module")  # type: ignore[misc]
def g2config_fixture() -> g2config_grpc.G2ConfigGrpc:
    """
    Single engine object to use for all tests.
    """

    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    result = g2config_grpc.G2ConfigGrpc(grpc_channel=grpc_channel)
    return result


@pytest.fixture(name="g2_configmgr", scope="module")  # type: ignore[misc]
def g2configmgr_fixture() -> g2configmgr_grpc.G2ConfigMgrGrpc:
    """
    Single engine object to use for all tests.
    """

    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    result = g2configmgr_grpc.G2ConfigMgrGrpc(grpc_channel=grpc_channel)
    return result


@pytest.fixture(name="g2_engine", scope="module")  # type: ignore[misc]
def g2engine_fixture() -> g2engine_grpc.G2EngineGrpc:
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

export_json_entity_report_iterator_schema = {
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


g2_config_schema = {
    "G2_CONFIG": {
        "CFG_ETYPE": [
            {
                "ETYPE_ID": int,
                "ETYPE_CODE": str,
                "ETYPE_DESC": str,
            },
        ],
        "CFG_DSRC_INTEREST": [],
        "CFG_RCLASS": [
            {
                "RCLASS_ID": int,
                "RCLASS_CODE": str,
                "RCLASS_DESC": str,
                "IS_DISCLOSED": str,
            },
        ],
        "CFG_FTYPE": [
            {
                "FTYPE_ID": int,
                "FTYPE_CODE": Or(str, None),
                "FCLASS_ID": int,
                "FTYPE_FREQ": str,
                "FTYPE_EXCL": str,
                "FTYPE_STAB": str,
                "PERSIST_HISTORY": str,
                "USED_FOR_CAND": str,
                "DERIVED": str,
                "RTYPE_ID": int,
                "ANONYMIZE": str,
                "VERSION": int,
                "SHOW_IN_MATCH_KEY": str,
            },
        ],
        "CFG_FCLASS": [
            {
                "FCLASS_ID": int,
                "FCLASS_CODE": str,
            },
        ],
        "CFG_FBOM": [
            {
                "FTYPE_ID": int,
                "FELEM_ID": int,
                "EXEC_ORDER": int,
                "DISPLAY_LEVEL": int,
                "DISPLAY_DELIM": Or(str, None),
                "DERIVED": str,
            },
        ],
        "CFG_FELEM": [
            {
                "FELEM_ID": int,
                "FELEM_CODE": str,
                "TOKENIZE": str,
                "DATA_TYPE": str,
            },
        ],
        "CFG_DSRC": [
            {
                "DSRC_ID": int,
                "DSRC_CODE": str,
                "DSRC_DESC": str,
                "DSRC_RELY": int,
                "RETENTION_LEVEL": str,
                "CONVERSATIONAL": str,
            },
        ],
        "CFG_EFBOM": [
            {
                "EFCALL_ID": int,
                "FTYPE_ID": int,
                "FELEM_ID": int,
                "EXEC_ORDER": int,
                "FELEM_REQ": str,
            },
        ],
        "CFG_EFUNC": [
            {
                "EFUNC_ID": int,
                "EFUNC_CODE": str,
                "FUNC_LIB": str,
                "FUNC_VER": str,
                "CONNECT_STR": str,
                "LANGUAGE": Or(str, None),
                "JAVA_CLASS_NAME": Or(str, None),
            },
        ],
        "CFG_EFCALL": [
            {
                "EFCALL_ID": int,
                "FTYPE_ID": int,
                "FELEM_ID": int,
                "EFUNC_ID": int,
                "EXEC_ORDER": int,
                "EFEAT_FTYPE_ID": int,
                "IS_VIRTUAL": str,
            },
        ],
        "CFG_SFCALL": [
            {
                "SFCALL_ID": int,
                "FTYPE_ID": int,
                "FELEM_ID": int,
                "SFUNC_ID": int,
                "EXEC_ORDER": int,
            },
        ],
        "CFG_SFUNC": [
            {
                "SFUNC_ID": int,
                "SFUNC_CODE": str,
                "FUNC_LIB": str,
                "FUNC_VER": str,
                "CONNECT_STR": str,
                "LANGUAGE": Or(str, None),
                "JAVA_CLASS_NAME": Or(str, None),
            },
        ],
        "SYS_OOM": [
            {
                "OOM_TYPE": str,
                "OOM_LEVEL": str,
                "FTYPE_ID": int,
                "THRESH1_CNT": int,
                "THRESH1_OOM": int,
                "NEXT_THRESH": int,
            },
        ],
        "CFG_CFUNC": [
            {
                "CFUNC_ID": int,
                "CFUNC_CODE": str,
                "FUNC_LIB": str,
                "FUNC_VER": str,
                "CONNECT_STR": str,
                "ANON_SUPPORT": str,
                "LANGUAGE": Or(str, None),
                "JAVA_CLASS_NAME": Or(str, None),
            },
        ],
        "CFG_CFCALL": [
            {
                "CFCALL_ID": int,
                "FTYPE_ID": int,
                "CFUNC_ID": int,
                "EXEC_ORDER": int,
            },
        ],
        "CFG_GPLAN": [
            {
                "GPLAN_ID": int,
                "GPLAN_CODE": str,
            },
        ],
        "CFG_ERRULE": [
            {
                "ERRULE_ID": int,
                "ERRULE_CODE": str,
                "ERRULE_DESC": str,
                "RESOLVE": str,
                "RELATE": str,
                "REF_SCORE": int,
                "RTYPE_ID": int,
                "QUAL_ERFRAG_CODE": str,
                "DISQ_ERFRAG_CODE": Or(str, None),
                "ERRULE_TIER": Or(int, None),
            },
        ],
        "CFG_ERFRAG": [
            {
                "ERFRAG_ID": int,
                "ERFRAG_CODE": str,
                "ERFRAG_DESC": str,
                "ERFRAG_SOURCE": str,
                "ERFRAG_DEPENDS": Or(str, None),
            },
        ],
        "CFG_CFBOM": [
            {
                "CFCALL_ID": int,
                "FTYPE_ID": int,
                "FELEM_ID": int,
                "EXEC_ORDER": int,
            },
        ],
        "CFG_DFUNC": [
            {
                "DFUNC_ID": int,
                "DFUNC_CODE": str,
                "FUNC_LIB": str,
                "FUNC_VER": str,
                "CONNECT_STR": str,
                "ANON_SUPPORT": str,
                "LANGUAGE": Or(str, None),
                "JAVA_CLASS_NAME": Or(str, None),
            },
        ],
        "CFG_DFCALL": [
            {
                "DFCALL_ID": int,
                "FTYPE_ID": int,
                "DFUNC_ID": int,
                "EXEC_ORDER": int,
            },
        ],
        "CFG_DFBOM": [
            {
                "DFCALL_ID": int,
                "FTYPE_ID": int,
                "FELEM_ID": int,
                "EXEC_ORDER": int,
            },
        ],
        "CFG_CFRTN": [
            {
                "CFRTN_ID": int,
                "CFUNC_ID": int,
                "FTYPE_ID": int,
                "CFUNC_RTNVAL": str,
                "EXEC_ORDER": int,
                "SAME_SCORE": int,
                "CLOSE_SCORE": int,
                "LIKELY_SCORE": int,
                "PLAUSIBLE_SCORE": int,
                "UN_LIKELY_SCORE": int,
            },
        ],
        "CFG_RTYPE": [
            {
                "RTYPE_ID": int,
                "RTYPE_CODE": str,
                "RCLASS_ID": int,
                "REL_STRENGTH": int,
                "BREAK_RES": str,
            },
        ],
        "CFG_GENERIC_THRESHOLD": [
            {
                "GPLAN_ID": int,
                "BEHAVIOR": str,
                "FTYPE_ID": int,
                "CANDIDATE_CAP": int,
                "SCORING_CAP": int,
                "SEND_TO_REDO": str,
            },
        ],
        "CFG_FBOVR": [
            {
                "FTYPE_ID": int,
                "UTYPE_CODE": str,
                "FTYPE_FREQ": str,
                "FTYPE_EXCL": str,
                "FTYPE_STAB": str,
            },
        ],
        "CFG_ATTR": [
            {
                "ATTR_ID": int,
                "ATTR_CODE": str,
                "ATTR_CLASS": str,
                "FTYPE_CODE": Or(str, None),
                "FELEM_CODE": Or(str, None),
                "FELEM_REQ": str,
                "DEFAULT_VALUE": Or(str, None),
                "ADVANCED": str,
                "INTERNAL": str,
            },
        ],
        "CONFIG_BASE_VERSION": {
            "VERSION": str,
            "BUILD_VERSION": str,
            "BUILD_DATE": str,
            "BUILD_NUMBER": str,
            "COMPATIBILITY_VERSION": {
                "CONFIG_VERSION": str,
            },
        },
    },
}

# -----------------------------------------------------------------------------
# G2Engine testcases
# -----------------------------------------------------------------------------


def test_constructor() -> None:
    """Test constructor."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    actual = g2engine_grpc.G2EngineGrpc(grpc_channel=grpc_channel)
    assert isinstance(actual, g2engine_grpc.G2EngineGrpc)


def test_add_record(g2_engine: g2engine_grpc.G2EngineGrpc) -> None:
    """Test G2Engine().add_record()."""
    data_source_code = "TEST"
    record_id = "1"
    json_data: Dict[Any, Any] = {}
    load_id = "Test Load"
    g2_engine.add_record(data_source_code, record_id, json_data, load_id)


def test_add_record_bad_data_source_code_type(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().add_record()."""
    data_source_code = 1
    record_id = "1"
    json_data: Dict[Any, Any] = {}
    load_id = "Test Load"
    with pytest.raises(TypeError):
        g2_engine.add_record(
            data_source_code, record_id, json_data, load_id  # type: ignore[arg-type]
        )


def test_add_record_bad_data_source_code_value(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().add_record()."""
    data_source_code = "DOESN'T EXIST"
    record_id = "1"
    json_data: Dict[Any, Any] = {}
    load_id = "Test Load"
    with pytest.raises(G2UnknownDatasourceError):
        g2_engine.add_record(data_source_code, record_id, json_data, load_id)


def test_add_record_with_info(g2_engine: g2engine_grpc.G2EngineGrpc) -> None:
    """Test G2Engine().add_record_with_info()."""
    data_source_code = "TEST"
    record_id = "1"
    json_data: Dict[Any, Any] = {}
    load_id = "Test Load"
    actual = g2_engine.add_record_with_info(
        data_source_code, record_id, json_data, load_id
    )
    actual_json = json.loads(actual)
    assert schema(add_record_with_info_schema) == actual_json


def test_add_record_with_info_bad_data_source_code_type(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().add_record_with_info()."""
    data_source_code = 1
    record_id = "1"
    json_data: Dict[Any, Any] = {}
    load_id = "Test Load"
    with pytest.raises(TypeError):
        _ = g2_engine.add_record_with_info(
            data_source_code, record_id, json_data, load_id  # type: ignore[arg-type]
        )


def test_add_record_with_info_bad_data_source_code_value(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().add_record_with_info()."""
    data_source_code = "DOESN'T EXIST"
    record_id = "1"
    json_data: Dict[Any, Any] = {}
    load_id = "Test Load"
    with pytest.raises(G2UnknownDatasourceError):
        _ = g2_engine.add_record_with_info(
            data_source_code, record_id, json_data, load_id
        )


def test_count_redo_records(g2_engine: g2engine_grpc.G2EngineGrpc) -> None:
    """Test G2Engine().count_redo_records()."""
    actual = g2_engine.count_redo_records()
    assert actual == 0


def test_export_config_and_config_id(g2_engine: g2engine_grpc.G2EngineGrpc) -> None:
    """Test G2Engine().export_config_and_config_id()."""
    actual, actual_id = g2_engine.export_config_and_config_id()
    actual_json = json.loads(actual)
    assert actual_id > 0
    assert schema(g2_config_schema) == actual_json


def test_export_config(g2_engine: g2engine_grpc.G2EngineGrpc) -> None:
    """Test G2Engine().export_config()."""
    actual = g2_engine.export_config()
    actual_json = json.loads(actual)
    assert schema(g2_config_schema) == actual_json


def test_export_csv_entity_report(g2_engine: g2engine_grpc.G2EngineGrpc) -> None:
    """Test G2Engine().export_config()."""
    csv_headers = "RESOLVED_ENTITY_ID,RESOLVED_ENTITY_NAME,RELATED_ENTITY_ID,MATCH_LEVEL,MATCH_KEY,IS_DISCLOSED,IS_AMBIGUOUS,DATA_SOURCE,RECORD_ID,JSON_DATA,LAST_SEEN_DT,NAME_DATA,ATTRIBUTE_DATA,IDENTIFIER_DATA,ADDRESS_DATA,PHONE_DATA,RELATIONSHIP_DATA,ENTITY_DATA,OTHER_DATA"
    handle = g2_engine.export_csv_entity_report(csv_headers)
    actual = ""
    while True:
        fragment = g2_engine.fetch_next(handle)
        if len(fragment) == 0:
            break
        actual += fragment
    g2_engine.close_export(handle)
    assert len(actual) > 0


def test_export_csv_entity_report_iterator(
    g2_engine: g2engine_grpc.G2EngineGrpc,
    g2_configmgr: g2configmgr_grpc.G2ConfigMgrGrpc,
    g2_config: g2config_grpc.G2ConfigGrpc,
) -> None:
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
            customer.get("DataSource", ""),
            customer.get("Id", ""),
            customer.get("Json", ""),
            load_id,
        )

    # Test export.

    expected = [
        "RESOLVED_ENTITY_ID,RELATED_ENTITY_ID,MATCH_LEVEL,MATCH_KEY,DATA_SOURCE,RECORD_ID",
        '1,0,0,"","TEST","1"',
        '100001,0,0,"","CUSTOMERS","1001"',
        '100001,0,1,"+NAME+DOB+PHONE","CUSTOMERS","1002"',
        '100001,0,1,"+NAME+DOB+EMAIL","CUSTOMERS","1003"',
    ]

    i = 0
    for actual in g2_engine.export_csv_entity_report_iterator():
        assert actual.strip() == expected[i]
        i += 1
    assert i == len(expected)

    # Run again to make sure it starts from beginning.

    i = 0
    for _ in g2_engine.export_csv_entity_report_iterator():
        i += 1
    assert i == len(expected)

    # Delete records.

    for customer_id in customer_ids:
        customer = TRUTHSET_CUSTOMER_RECORDS.get(customer_id, {})
        g2_engine.delete_record(
            customer.get("DataSource", ""),
            customer.get("Id", ""),
            load_id,
        )

    # Test export, again.

    expected = [
        "RESOLVED_ENTITY_ID,RELATED_ENTITY_ID,MATCH_LEVEL,MATCH_KEY,DATA_SOURCE,RECORD_ID",
        '1,0,0,"","TEST","1"',
    ]

    i = 0
    for actual in g2_engine.export_csv_entity_report_iterator():
        assert actual.strip() == expected[i]
        i += 1
    assert i == len(expected)


def test_export_json_entity_report(g2_engine: g2engine_grpc.G2EngineGrpc) -> None:
    """Test G2Engine().export_json_entity_report()."""
    handle = g2_engine.export_json_entity_report()
    actual = ""
    while True:
        fragment = g2_engine.fetch_next(handle)
        if len(fragment) == 0:
            break
        actual += fragment
    g2_engine.close_export(handle)
    actual_json = json.loads(actual)
    assert schema(export_json_entity_report_iterator_schema) == actual_json


def test_export_json_entity_report_iterator(
    g2_engine: g2engine_grpc.G2EngineGrpc,
    g2_configmgr: g2configmgr_grpc.G2ConfigMgrGrpc,
    g2_config: g2config_grpc.G2ConfigGrpc,
) -> None:
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
            customer.get("DataSource", ""),
            customer.get("Id", ""),
            customer.get("Json", ""),
            load_id,
        )

    # Test export.

    i = 0
    for actual in g2_engine.export_json_entity_report_iterator():
        i += 1
        actual_json = json.loads(actual)
        assert schema(export_json_entity_report_iterator_schema) == actual_json
    assert i == 2

    # Delete records.

    for customer_id in customer_ids:
        customer = TRUTHSET_CUSTOMER_RECORDS.get(customer_id, {})
        g2_engine.delete_record(
            customer.get("DataSource", ""),
            customer.get("Id", ""),
            load_id,
        )

    # Test export, again.

    i = 0
    for actual in g2_engine.export_json_entity_report_iterator():
        i += 1
        actual_json = json.loads(actual)
        assert schema(export_json_entity_report_iterator_schema) == actual_json
    assert i == 1


# -----------------------------------------------------------------------------
# G2Engine tests using Truth Set
# -----------------------------------------------------------------------------


def test_setup_truth_set(g2_engine: g2engine_grpc.G2EngineGrpc) -> None:
    record_sets = [
        TRUTHSET_CUSTOMER_RECORDS,
        TRUTHSET_REFERENCE_RECORDS,
        TRUTHSET_WATCHLIST_RECORDS,
    ]
    for record_set in record_sets:
        for record in record_set.values():
            g2_engine.add_record(
                str(record.get("DataSource")),
                str(record.get("Id")),
                str(record.get("Json")),
            )


def test_find_interesting_entities_by_entity_id(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().export_config()."""
    record = TRUTHSET_CUSTOMER_RECORDS.get("1001", {})
    entity_json = g2_engine.get_entity_by_record_id(
        record.get("DataSource", ""), record.get("Id", "")
    )
    entity = json.loads(entity_json)
    actual = g2_engine.find_interesting_entities_by_entity_id(
        entity.get("RESOLVED_ENTITY", {}).get("ENTITY_ID", 0)
    )
    actual_json = json.loads(actual)
    print(f">>>>>>>> {actual_json}")


# -----------------------------------------------------------------------------
# G2Engine misc
# -----------------------------------------------------------------------------


def test_add_record_using_context_managment() -> None:
    """Test the use of G2EngineGrpc in context."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    with g2engine_grpc.G2EngineGrpc(grpc_channel=grpc_channel) as g2_engine:
        data_source_code = "TEST"
        record_id = "2"
        json_data = "{}"
        load_id = "Test Load"
        g2_engine.add_record(data_source_code, record_id, json_data, load_id)
