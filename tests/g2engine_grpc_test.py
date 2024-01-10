import json
from typing import Any, Dict, List, Tuple

import grpc
import pytest
from pytest_schema import Or, schema
from senzing_truthset import (
    TRUTHSET_CUSTOMER_RECORDS,
    TRUTHSET_DATASOURCES,
    TRUTHSET_REFERENCE_RECORDS,
    TRUTHSET_WATCHLIST_RECORDS,
)

from senzing_grpc import (
    G2NotFoundError,
    G2UnknownDatasourceError,
    g2config_grpc,
    g2configmgr_grpc,
    g2engine_grpc,
)

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

DATA_SOURCES = {
    "CUSTOMERS": TRUTHSET_CUSTOMER_RECORDS,
    "REFERENCE": TRUTHSET_REFERENCE_RECORDS,
    "WATCHLIST": TRUTHSET_WATCHLIST_RECORDS,
}

LOAD_ID = "Test Load"

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
    "AFFECTED_ENTITIES": [{"ENTITY_ID": int}],
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

how_results_schema = {
    "HOW_RESULTS": {
        "RESOLUTION_STEPS": [],
        "FINAL_STATE": {
            "NEED_REEVALUATION": int,
            "VIRTUAL_ENTITIES": [
                {
                    "VIRTUAL_ENTITY_ID": str,
                    "MEMBER_RECORDS": [
                        {
                            "INTERNAL_ID": int,
                            "RECORDS": [{"DATA_SOURCE": str, "RECORD_ID": str}],
                        }
                    ],
                }
            ],
        },
    }
}

interesting_entities_schema = {
    "INTERESTING_ENTITIES": {"ENTITIES": []},
}

network_schema = {
    "ENTITY_PATHS": [],
    "ENTITIES": [
        {
            "RESOLVED_ENTITY": {
                "ENTITY_ID": int,
                "ENTITY_NAME": str,
                "RECORD_SUMMARY": [
                    {
                        "DATA_SOURCE": str,
                        "RECORD_COUNT": int,
                        "FIRST_SEEN_DT": str,
                        "LAST_SEEN_DT": str,
                    }
                ],
                "LAST_SEEN_DT": str,
            },
            "RELATED_ENTITIES": [],
        }
    ],
}

path_schema = {
    "ENTITY_PATHS": [{"START_ENTITY_ID": int, "END_ENTITY_ID": int, "ENTITIES": [int]}],
    "ENTITIES": [
        {
            "RESOLVED_ENTITY": {
                "ENTITY_ID": int,
                "ENTITY_NAME": str,
                "RECORD_SUMMARY": [
                    {
                        "DATA_SOURCE": str,
                        "RECORD_COUNT": int,
                        "FIRST_SEEN_DT": str,
                        "LAST_SEEN_DT": str,
                    }
                ],
                "LAST_SEEN_DT": str,
            },
            "RELATED_ENTITIES": [],
        }
    ],
}


process_withinfo_schema = {
    "DATA_SOURCE": str,
    "RECORD_ID": str,
    "AFFECTED_ENTITIES": [{"ENTITY_ID": int}],
    "INTERESTING_ENTITIES": {"ENTITIES": []},
}

record_schema = {"DATA_SOURCE": str, "RECORD_ID": str, "JSON_DATA": {}}

redo_record_schema = {
    "REASON": str,
    "DATA_SOURCE": str,
    "RECORD_ID": str,
    "ENTITY_TYPE": str,
    "DSRC_ACTION": str,
}

resolved_entity_schema = {
    "RESOLVED_ENTITY": {
        "ENTITY_ID": int,
        "ENTITY_NAME": str,
        "FEATURES": {},
        "RECORD_SUMMARY": [
            {
                "DATA_SOURCE": str,
                "RECORD_COUNT": int,
                "FIRST_SEEN_DT": str,
                "LAST_SEEN_DT": str,
            }
        ],
        "LAST_SEEN_DT": str,
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
            },
        ],
    },
    "RELATED_ENTITIES": [],
}

search_schema = {
    "RESOLVED_ENTITIES": [
        {
            "MATCH_INFO": {
                "MATCH_LEVEL": int,
                "MATCH_LEVEL_CODE": str,
                "MATCH_KEY": str,
                "ERRULE_CODE": str,
                "FEATURE_SCORES": {},
            },
            "ENTITY": {
                "RESOLVED_ENTITY": {
                    "ENTITY_ID": int,
                    "ENTITY_NAME": str,
                    "FEATURES": {},
                    "RECORD_SUMMARY": [
                        {
                            "DATA_SOURCE": str,
                            "RECORD_COUNT": int,
                            "FIRST_SEEN_DT": str,
                            "LAST_SEEN_DT": str,
                        }
                    ],
                    "LAST_SEEN_DT": str,
                }
            },
        }
    ]
}

stats_schema = {
    "workload": {
        "apiVersion": str,
        "loadedRecords": int,
        "addedRecords": int,
        "deletedRecords": int,
        "reevaluations": int,
        "repairedEntities": int,
        "duration": int,
        "retries": int,
        "candidates": int,
        "actualAmbiguousTest": int,
        "cachedAmbiguousTest": int,
        "libFeatCacheHit": int,
        "libFeatCacheMiss": int,
        "resFeatStatCacheHit": int,
        "resFeatStatCacheMiss": int,
        "resFeatStatUpdate": int,
        "unresolveTest": int,
        "abortedUnresolve": int,
        "gnrScorersUsed": int,
        "unresolveTriggers": {},
        "reresolveTriggers": {},
        "reresolveSkipped": int,
        "filteredObsFeat": int,
        "expressedFeatureCalls": [{}],
        "expressedFeaturesCreated": [{}],
        "scoredPairs": [{}],
        "cacheHit": [{}],
        "cacheMiss": [{}],
        "redoTriggers": [{}],
        "latchContention": [],
        "highContentionFeat": [],
        "highContentionResEnt": [],
        "genericDetect": [],
        "candidateBuilders": [{}],
        "suppressedCandidateBuilders": [],
        "suppressedScoredFeatureType": [],
        "reducedScoredFeatureType": [],
        "suppressedDisclosedRelationshipDomainCount": int,
        "CorruptEntityTestDiagnosis": {},
        "threadState": {},
        "systemResources": {},
    }
}

virtual_entity_schema = {
    "RESOLVED_ENTITY": {
        "ENTITY_ID": int,
        "ENTITY_NAME": str,
        "FEATURES": {},
        "RECORD_SUMMARY": [
            {
                "DATA_SOURCE": str,
                "RECORD_COUNT": int,
                "FIRST_SEEN_DT": str,
                "LAST_SEEN_DT": str,
            }
        ],
        "LAST_SEEN_DT": str,
        "RECORDS": [
            {
                "DATA_SOURCE": str,
                "RECORD_ID": str,
                "ENTITY_TYPE": str,
                "INTERNAL_ID": int,
                "ENTITY_KEY": str,
                "ENTITY_DESC": str,
                "LAST_SEEN_DT": str,
                "FEATURES": [{"LIB_FEAT_ID": int}],
            },
        ],
    },
}

why_entities_results_schema = {
    "WHY_RESULTS": [
        {
            "ENTITY_ID": int,
            "ENTITY_ID_2": int,
            "MATCH_INFO": {},
        }
    ],
    "ENTITIES": [
        {
            "RESOLVED_ENTITY": {
                "ENTITY_ID": int,
                "ENTITY_NAME": str,
                "FEATURES": {},
                "RECORD_SUMMARY": [{}],
                "LAST_SEEN_DT": str,
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
                        "FEATURES": [{}],
                    }
                ],
            },
            "RELATED_ENTITIES": [{}],
        }
    ],
}


why_entity_results_schema = {
    "WHY_RESULTS": [
        {
            "INTERNAL_ID": int,
            "ENTITY_ID": int,
            "FOCUS_RECORDS": [{}],
            "MATCH_INFO": {
                "WHY_KEY": str,
                "WHY_ERRULE_CODE": str,
                "MATCH_LEVEL_CODE": str,
                "CANDIDATE_KEYS": {},
                "FEATURE_SCORES": {},
            },
        }
    ],
    "ENTITIES": [
        {
            "RESOLVED_ENTITY": {
                "ENTITY_ID": int,
                "ENTITY_NAME": str,
                "FEATURES": {},
                "RECORD_SUMMARY": [{}],
                "LAST_SEEN_DT": str,
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
                        "FEATURES": [{}],
                    }
                ],
            },
            "RELATED_ENTITIES": [{}],
        }
    ],
}


# -----------------------------------------------------------------------------
# Utilities
# -----------------------------------------------------------------------------


def add_records(
    g2_engine: g2engine_grpc.G2EngineGrpc, record_id_list: List[Tuple[str, str]]
) -> None:
    for record_id in record_id_list:
        datasource = record_id[0]
        record_id = record_id[1]
        record = DATA_SOURCES.get(datasource, {}).get(record_id, {})
        g2_engine.add_record(
            record.get("DataSource", ""),
            record.get("Id", ""),
            record.get("Json", ""),
            LOAD_ID,
        )


def add_records_truthset(g2_engine: g2engine_grpc.G2EngineGrpc) -> None:
    for record_set in DATA_SOURCES.values():
        for record in record_set.values():
            g2_engine.add_record(
                record.get("DataSource"), record.get("Id"), record.get("Json"), LOAD_ID
            )
    while g2_engine.count_redo_records() > 0:
        record = g2_engine.get_redo_record()
        g2_engine.process(record)


def delete_records(
    g2_engine: g2engine_grpc.G2EngineGrpc, record_id_list: List[Tuple[str, str]]
) -> None:
    for record_id in record_id_list:
        datasource = record_id[0]
        record_id = record_id[1]
        record = DATA_SOURCES.get(datasource, {}).get(record_id, {})
        g2_engine.delete_record(
            record.get("DataSource", ""),
            record.get("Id", ""),
            LOAD_ID,
        )


def delete_records_truthset(g2_engine: g2engine_grpc.G2EngineGrpc) -> None:
    for record_set in DATA_SOURCES.values():
        for record in record_set.values():
            g2_engine.delete_record(record.get("DataSource"), record.get("Id"), LOAD_ID)


def get_entity_id_from_record_id(
    g2_engine: g2engine_grpc.G2EngineGrpc, data_source_code: str, record_id: str
) -> int:
    entity_json = g2_engine.get_entity_by_record_id(data_source_code, record_id)
    entity = json.loads(entity_json)
    return entity.get("RESOLVED_ENTITY", {}).get("ENTITY_ID", 0)


# -----------------------------------------------------------------------------
# G2Engine pre tests
# -----------------------------------------------------------------------------


def test_constructor() -> None:
    """Test constructor."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    actual = g2engine_grpc.G2EngineGrpc(grpc_channel=grpc_channel)
    assert isinstance(actual, g2engine_grpc.G2EngineGrpc)


def test_add_truthset_datasources(
    g2_engine: g2engine_grpc.G2EngineGrpc,
    g2_configmgr: g2configmgr_grpc.G2ConfigMgrGrpc,
    g2_config: g2config_grpc.G2ConfigGrpc,
) -> None:
    config_handle = g2_config.create()
    for _, value in TRUTHSET_DATASOURCES.items():
        g2_config.add_data_source(config_handle, value.get("Json", ""))
    json_config = g2_config.save(config_handle)
    new_config_id = g2_configmgr.add_config(json_config, "Test")
    g2_configmgr.set_default_config_id(new_config_id)
    g2_engine.reinit(new_config_id)


# -----------------------------------------------------------------------------
# G2Engine testcases
# -----------------------------------------------------------------------------


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
    actual_dict = json.loads(actual)
    assert schema(add_record_with_info_schema) == actual_dict


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


def test_close_export(g2_engine: g2engine_grpc.G2EngineGrpc) -> None:
    """Test G2Engine().close_export()."""
    pass


def test_count_redo_records(g2_engine: g2engine_grpc.G2EngineGrpc) -> None:
    """Test G2Engine().count_redo_records()."""
    actual = g2_engine.count_redo_records()
    assert actual == 0


def test_delete_record(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().delete_record()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
    ]
    add_records(g2_engine, test_records)
    g2_engine.delete_record("CUSTOMERS", "1001")


def test_delete_record_with_info(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().delete_record_with_info()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
    ]
    add_records(g2_engine, test_records)
    actual = g2_engine.delete_record_with_info("CUSTOMERS", "1001")
    actual_dict = json.loads(actual)
    assert schema(add_record_with_info_schema) == actual_dict


def test_export_config(g2_engine: g2engine_grpc.G2EngineGrpc) -> None:
    """Test G2Engine().export_config()."""
    actual = g2_engine.export_config()
    actual_dict = json.loads(actual)
    assert schema(g2_config_schema) == actual_dict


def test_export_config_and_config_id(g2_engine: g2engine_grpc.G2EngineGrpc) -> None:
    """Test G2Engine().export_config_and_config_id()."""
    actual, actual_id = g2_engine.export_config_and_config_id()
    actual_dict = json.loads(actual)
    assert actual_id > 0
    assert schema(g2_config_schema) == actual_dict


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
    """Test G2Engine().export_csv_entity_report_iterator()."""

    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
        ("CUSTOMERS", "1003"),
    ]
    add_records(g2_engine, test_records)

    # Test export.

    expected = [
        "RESOLVED_ENTITY_ID,RELATED_ENTITY_ID,MATCH_LEVEL,MATCH_KEY,DATA_SOURCE,RECORD_ID",
        '1,0,0,"","TEST","1"',
        '4,0,0,"","CUSTOMERS","1001"',
        '4,0,1,"+NAME+DOB+PHONE","CUSTOMERS","1002"',
        '4,0,1,"+NAME+DOB+EMAIL","CUSTOMERS","1003"',
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

    delete_records(g2_engine, test_records)

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
    actual_dict = json.loads(actual)
    assert schema(export_json_entity_report_iterator_schema) == actual_dict


def test_export_json_entity_report_iterator(
    g2_engine: g2engine_grpc.G2EngineGrpc,
    g2_configmgr: g2configmgr_grpc.G2ConfigMgrGrpc,
    g2_config: g2config_grpc.G2ConfigGrpc,
) -> None:
    """Test G2Engine().export_json_entity_report_iterator()."""

    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
        ("CUSTOMERS", "1003"),
    ]
    add_records(g2_engine, test_records)

    # Test export.

    i = 0
    for actual in g2_engine.export_json_entity_report_iterator():
        i += 1
        actual_dict = json.loads(actual)
        assert schema(export_json_entity_report_iterator_schema) == actual_dict
    assert i == 2

    delete_records(g2_engine, test_records)

    # Test export, again.

    i = 0
    for actual in g2_engine.export_json_entity_report_iterator():
        i += 1
        actual_dict = json.loads(actual)
        assert schema(export_json_entity_report_iterator_schema) == actual_dict
    assert i == 1


def test_fetch_next(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().fetch_next."""
    pass


def test_find_interesting_entities_by_entity_id(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().find_interesting_entities_by_entity_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
    ]
    add_records(g2_engine, test_records)
    entity_id = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    actual = g2_engine.find_interesting_entities_by_entity_id(entity_id)
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(interesting_entities_schema) == actual_dict


def test_find_interesting_entities_by_record_id(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().find_interesting_entities_by_record_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
    ]
    add_records(g2_engine, test_records)
    actual = g2_engine.find_interesting_entities_by_record_id("CUSTOMERS", "1001")
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(interesting_entities_schema) == actual_dict


def test_find_network_by_entity_id(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().find_network_by_entity_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
    ]
    add_records(g2_engine, test_records)
    entity_id_1 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    entity_id_2 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1002")
    entity_list = {
        "ENTITIES": [
            {"ENTITY_ID": entity_id_1},
            {"ENTITY_ID": entity_id_2},
        ]
    }
    max_degree = 2
    build_out_degree = 1
    max_entities = 10
    actual = g2_engine.find_network_by_entity_id(
        entity_list,
        max_degree,
        build_out_degree,
        max_entities,
    )
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(network_schema) == actual_dict


def test_find_network_by_entity_id_v2(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().find_network_by_entity_id_v2()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
    ]
    add_records(g2_engine, test_records)
    entity_id_1 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    entity_id_2 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1002")
    entity_list = {
        "ENTITIES": [
            {"ENTITY_ID": entity_id_1},
            {"ENTITY_ID": entity_id_2},
        ]
    }
    max_degree = 2
    build_out_degree = 1
    max_entities = 10
    flags = -1
    actual = g2_engine.find_network_by_entity_id_v2(
        entity_list,
        max_degree,
        build_out_degree,
        max_entities,
        flags,
    )
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(network_schema) == actual_dict


def test_find_network_by_record_id(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().find_network_by_entity_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
    ]
    add_records(g2_engine, test_records)
    entity_id_1 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    entity_id_2 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1002")
    entity_list = {
        "ENTITIES": [
            {"ENTITY_ID": entity_id_1},
            {"ENTITY_ID": entity_id_2},
        ]
    }
    max_degree = 2
    build_out_degree = 1
    max_entities = 10
    actual = g2_engine.find_network_by_entity_id(
        entity_list,
        max_degree,
        build_out_degree,
        max_entities,
    )
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(network_schema) == actual_dict


def test_find_network_by_record_id_v2(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().find_network_by_entity_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
    ]
    add_records(g2_engine, test_records)
    entity_id_1 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    entity_id_2 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1002")
    entity_list = {
        "ENTITIES": [
            {"ENTITY_ID": entity_id_1},
            {"ENTITY_ID": entity_id_2},
        ]
    }
    max_degree = 2
    build_out_degree = 1
    max_entities = 10
    flags = -1
    actual = g2_engine.find_network_by_entity_id(
        entity_list,
        max_degree,
        build_out_degree,
        max_entities,
        flags,
    )
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(network_schema) == actual_dict


def test_find_path_by_entity_id(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().find_path_by_entity_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
    ]
    add_records(g2_engine, test_records)
    entity_id_1 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    entity_id_2 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1002")
    max_degree = 1
    actual = g2_engine.find_path_by_entity_id(
        entity_id_1,
        entity_id_2,
        max_degree,
    )
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(path_schema) == actual_dict


def test_find_path_by_entity_id_v2(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().find_path_by_entity_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
    ]
    add_records(g2_engine, test_records)
    entity_id_1 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    entity_id_2 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1002")
    max_degree = 1
    flags = -1
    actual = g2_engine.find_path_by_entity_id(
        entity_id_1,
        entity_id_2,
        max_degree,
        flags,
    )
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(path_schema) == actual_dict


def test_find_path_by_record_id(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().find_path_by_record_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
    ]
    add_records(g2_engine, test_records)
    max_degree = 1
    actual = g2_engine.find_path_by_record_id(
        "CUSTOMERS",
        "1001",
        "CUSTOMERS",
        "1002",
        max_degree,
    )
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(path_schema) == actual_dict


def test_find_path_by_record_id_v2(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().find_path_by_record_id_v2()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
    ]
    add_records(g2_engine, test_records)
    max_degree = 1
    flags = -1
    actual = g2_engine.find_path_by_record_id_v2(
        "CUSTOMERS",
        "1001",
        "CUSTOMERS",
        "1002",
        max_degree,
        flags,
    )
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(path_schema) == actual_dict


def test_find_path_excluding_by_entity_id(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().find_path_excluding_by_entity_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
        ("CUSTOMERS", "1003"),
    ]
    add_records(g2_engine, test_records)
    entity_id_1 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    entity_id_2 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1002")
    entity_id_3 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1003")
    max_degree = 1
    excluded_entities = {
        "ENTITIES": [{"ENTITY_ID": entity_id_3}],
    }
    actual = g2_engine.find_path_excluding_by_entity_id(
        entity_id_1,
        entity_id_2,
        max_degree,
        excluded_entities,
    )
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(path_schema) == actual_dict


def test_find_path_excluding_by_entity_id_v2(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().find_path_excluding_by_entity_id_v2()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
        ("CUSTOMERS", "1003"),
    ]
    add_records(g2_engine, test_records)
    entity_id_1 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    entity_id_2 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1002")
    entity_id_3 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1003")
    max_degree = 1
    excluded_entities = {
        "ENTITIES": [{"ENTITY_ID": entity_id_3}],
    }
    flags = -1
    actual = g2_engine.find_path_excluding_by_entity_id_v2(
        entity_id_1,
        entity_id_2,
        max_degree,
        excluded_entities,
        flags,
    )
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(path_schema) == actual_dict


def test_find_path_excluding_by_record_id(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().find_path_excluding_by_record_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
        ("CUSTOMERS", "1003"),
    ]
    add_records(g2_engine, test_records)
    max_degree = 1
    excluded_records = {
        "RECORDS": [{"DATA_SOURCE": "CUSTOMERS", "RECORD_ID": "1003"}],
    }
    actual = g2_engine.find_path_excluding_by_record_id(
        "CUSTOMERS",
        "1001",
        "CUSTOMERS",
        "1002",
        max_degree,
        excluded_records,
    )
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(path_schema) == actual_dict


def test_find_path_excluding_by_record_id_v2(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().find_path_excluding_by_record_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
        ("CUSTOMERS", "1003"),
    ]
    add_records(g2_engine, test_records)
    max_degree = 1
    excluded_records = {
        "RECORDS": [{"DATA_SOURCE": "CUSTOMERS", "RECORD_ID": "1003"}],
    }
    flags = -1
    actual = g2_engine.find_path_excluding_by_record_id(
        "CUSTOMERS",
        "1001",
        "CUSTOMERS",
        "1002",
        max_degree,
        excluded_records,
        flags,
    )
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(path_schema) == actual_dict


def test_find_path_including_source_by_entity_id(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().find_path_including_source_by_entity_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
        ("CUSTOMERS", "1003"),
    ]
    add_records(g2_engine, test_records)
    entity_id_1 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    entity_id_2 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1002")
    entity_id_3 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1003")
    max_degree = 1
    excluded_entities = {
        "ENTITIES": [{"ENTITY_ID": entity_id_3}],
    }
    required_dsrcs = {"DATA_SOURCES": ["CUSTOMERS"]}
    actual = g2_engine.find_path_including_source_by_entity_id(
        entity_id_1,
        entity_id_2,
        max_degree,
        excluded_entities,
        required_dsrcs,
    )
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(path_schema) == actual_dict


def test_find_path_including_source_by_entity_id_v2(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().find_path_including_source_by_entity_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
        ("CUSTOMERS", "1003"),
    ]
    add_records(g2_engine, test_records)
    entity_id_1 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    entity_id_2 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1002")
    entity_id_3 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1003")
    max_degree = 1
    excluded_entities = {
        "ENTITIES": [{"ENTITY_ID": entity_id_3}],
    }
    required_dsrcs = {"DATA_SOURCES": ["CUSTOMERS"]}
    flags = -1
    actual = g2_engine.find_path_including_source_by_entity_id(
        entity_id_1,
        entity_id_2,
        max_degree,
        excluded_entities,
        required_dsrcs,
        flags,
    )
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(path_schema) == actual_dict


def test_find_path_including_source_by_record_id(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().find_path_including_source_by_record_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
        ("CUSTOMERS", "1003"),
    ]
    add_records(g2_engine, test_records)
    entity_id_3 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1003")
    max_degree = 1
    excluded_entities = {
        "ENTITIES": [{"ENTITY_ID": entity_id_3}],
    }
    required_dsrcs = {"DATA_SOURCES": ["CUSTOMERS"]}
    actual = g2_engine.find_path_including_source_by_record_id(
        "CUSTOMERS",
        "1001",
        "CUSTOMERS",
        "1002",
        max_degree,
        excluded_entities,
        required_dsrcs,
    )
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(path_schema) == actual_dict


def test_find_path_including_source_by_record_id_v2(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().find_path_including_source_by_record_id_v2()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
        ("CUSTOMERS", "1003"),
    ]
    add_records(g2_engine, test_records)
    entity_id_3 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1003")
    max_degree = 1
    excluded_entities = {
        "ENTITIES": [{"ENTITY_ID": entity_id_3}],
    }
    required_dsrcs = {"DATA_SOURCES": ["CUSTOMERS"]}
    flags = -1
    actual = g2_engine.find_path_including_source_by_record_id_v2(
        "CUSTOMERS",
        "1001",
        "CUSTOMERS",
        "1002",
        max_degree,
        excluded_entities,
        required_dsrcs,
        flags,
    )
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(path_schema) == actual_dict


def test_get_active_config_id(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().get_active_config_id()."""
    actual = g2_engine.get_active_config_id()
    assert actual >= 0


def test_get_entity_by_entity_id(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().get_entity_by_entity_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
    ]
    add_records(g2_engine, test_records)
    entity_id = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    actual = g2_engine.get_entity_by_entity_id(entity_id)
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(resolved_entity_schema) == actual_dict


def test_get_entity_by_entity_id_v2(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().get_entity_by_entity_id_v2()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
    ]
    add_records(g2_engine, test_records)
    entity_id = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    flags = -1
    actual = g2_engine.get_entity_by_entity_id_v2(entity_id, flags)
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(resolved_entity_schema) == actual_dict


def test_get_entity_by_record_id(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().get_entity_by_record_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
    ]
    add_records(g2_engine, test_records)
    actual = g2_engine.get_entity_by_record_id("CUSTOMERS", "1001")
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(resolved_entity_schema) == actual_dict


def test_get_entity_by_record_id_bad_record_id(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().get_entity_by_record_id()."""

    with pytest.raises(G2NotFoundError):
        actual = g2_engine.get_entity_by_record_id("CUSTOMERS", "1001")
        actual_dict = json.loads(actual)
        assert schema(resolved_entity_schema) == actual_dict


def test_get_entity_by_record_id_v2(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().get_entity_by_record_id_v2()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
    ]
    add_records(g2_engine, test_records)
    flags = -1
    actual = g2_engine.get_entity_by_record_id_v2("CUSTOMERS", "1001", flags)
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(resolved_entity_schema) == actual_dict


def test_get_record(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().get_record()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
    ]
    add_records(g2_engine, test_records)
    actual = g2_engine.get_record("CUSTOMERS", "1001")
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(record_schema) == actual_dict


def test_get_record_v2(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().get_record_v2()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
    ]
    add_records(g2_engine, test_records)
    flags = -1
    actual = g2_engine.get_record_v2("CUSTOMERS", "1001", flags)
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(record_schema) == actual_dict


def test_get_redo_record(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().get_redo_record()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
        ("CUSTOMERS", "1003"),
    ]
    add_records(g2_engine, test_records)
    actual = g2_engine.get_redo_record()
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(redo_record_schema) == actual_dict


def test_get_repository_last_modified_time(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().get_repository_last_modified_time()."""
    actual = g2_engine.get_repository_last_modified_time()
    assert actual >= 0


def test_get_virtual_entity_by_record_id(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().get_virtual_entity_by_record_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
    ]
    add_records(g2_engine, test_records)
    record_list = {
        "RECORDS": [
            {"DATA_SOURCE": "CUSTOMERS", "RECORD_ID": "1001"},
            {"DATA_SOURCE": "CUSTOMERS", "RECORD_ID": "1002"},
        ]
    }
    actual = g2_engine.get_virtual_entity_by_record_id(record_list)
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(virtual_entity_schema) == actual_dict


def test_get_virtual_entity_by_record_id_v2(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().get_virtual_entity_by_record_id_v2()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
    ]
    add_records(g2_engine, test_records)
    record_list = {
        "RECORDS": [
            {"DATA_SOURCE": "CUSTOMERS", "RECORD_ID": "1001"},
            {"DATA_SOURCE": "CUSTOMERS", "RECORD_ID": "1002"},
        ]
    }
    flags = -1
    actual = g2_engine.get_virtual_entity_by_record_id_v2(record_list, flags)
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(virtual_entity_schema) == actual_dict


def test_how_entity_by_entity_id(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().how_entity_by_entity_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
    ]
    add_records(g2_engine, test_records)
    entity_id = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    actual = g2_engine.how_entity_by_entity_id(entity_id)
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(how_results_schema) == actual_dict


def test_how_entity_by_entity_id_v2(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().how_entity_by_entity_id_v2()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
    ]
    add_records(g2_engine, test_records)
    entity_id = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    flags = -1
    actual = g2_engine.how_entity_by_entity_id_v2(entity_id, flags)
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(how_results_schema) == actual_dict


def test_init(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().init()."""
    module_name = "Test"
    ini_params = {}
    g2_engine.init(module_name, ini_params)


def test_init_with_config_id(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().init_with_config_id()."""
    module_name = "Test"
    ini_params = {}
    init_config_id = 0
    g2_engine.init_with_config_id(module_name, ini_params, init_config_id)


def test_prime_engine(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().prime_engine()."""
    g2_engine.prime_engine()


def test_process(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().get_redo_record()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
        ("CUSTOMERS", "1003"),
    ]
    add_records(g2_engine, test_records)
    redo_records_processed = 0
    while g2_engine.count_redo_records() > 0:
        record = g2_engine.get_redo_record()
        g2_engine.process(record)
        redo_records_processed += 1
    delete_records(g2_engine, test_records)
    assert redo_records_processed > 0


def test_process_with_info(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().process_with_info()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
        ("CUSTOMERS", "1003"),
    ]
    add_records(g2_engine, test_records)
    flags = -1
    redo_records_processed = 0
    while g2_engine.count_redo_records() > 0:
        record = g2_engine.get_redo_record()
        actual = g2_engine.process_with_info(record, flags)
        actual_dict = json.loads(actual)
        assert schema(process_withinfo_schema) == actual_dict
        redo_records_processed += 1
    delete_records(g2_engine, test_records)
    assert redo_records_processed > 0


def test_purge_repository(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().purge_repository."""
    pass


def test_reevaluate_entity(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().get_entity_id_from_record_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
    ]
    add_records(g2_engine, test_records)
    entity_id = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    g2_engine.reevaluate_entity(entity_id)
    delete_records(g2_engine, test_records)


def test_reevaluate_entity_with_info(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().reevaluate_entity_with_info()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
    ]
    add_records(g2_engine, test_records)
    entity_id = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    flags = -1
    actual = g2_engine.reevaluate_entity_with_info(entity_id, flags)
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(add_record_with_info_schema) == actual_dict


def test_reevaluate_record(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().get_entity_id_from_record_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
    ]
    add_records(g2_engine, test_records)
    entity_id = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    g2_engine.reevaluate_entity(entity_id)
    delete_records(g2_engine, test_records)


def test_reevaluate_record_with_info(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().reevaluate_entity_with_info()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
    ]
    add_records(g2_engine, test_records)
    entity_id = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    actual = g2_engine.reevaluate_entity_with_info(entity_id)
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(add_record_with_info_schema) == actual_dict


def test_reinit(
    g2_engine: g2engine_grpc.G2EngineGrpc,
    g2_configmgr: g2configmgr_grpc.G2ConfigMgrGrpc,
) -> None:
    """Test G2Engine().reinit()."""
    init_config_id = g2_configmgr.get_default_config_id()
    g2_engine.reinit(init_config_id)


def test_replace_record(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().replace_record()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
    ]
    add_records(g2_engine, test_records)
    json_data = TRUTHSET_CUSTOMER_RECORDS.get("1001", {}).get("Json", "")
    data = json.loads(json_data)
    data["ADDR_POSTAL_CODE"] = "99999"
    g2_engine.replace_record("CUSTOMERS", "1001", data, LOAD_ID)
    delete_records(g2_engine, test_records)


def test_replace_record_with_info(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().replace_record_with_info()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
    ]
    add_records(g2_engine, test_records)
    json_data = TRUTHSET_CUSTOMER_RECORDS.get("1001", {}).get("Json", "")
    data = json.loads(json_data)
    data["ADDR_POSTAL_CODE"] = "99999"
    actual = g2_engine.replace_record_with_info("CUSTOMERS", "1001", data, LOAD_ID)
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(add_record_with_info_schema) == actual_dict


def test_search_by_attributes(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().search_by_attributes()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
        ("CUSTOMERS", "1003"),
    ]
    add_records(g2_engine, test_records)
    json_data = {"NAME_FULL": "BOB SMITH", "EMAIL_ADDRESS": "bsmith@work.com"}
    actual = g2_engine.search_by_attributes(json_data)
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(search_schema) == actual_dict


def test_search_by_attributes_v2(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().search_by_attributes_v2()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
        ("CUSTOMERS", "1003"),
    ]
    add_records(g2_engine, test_records)
    json_data = {"NAME_FULL": "BOB SMITH", "EMAIL_ADDRESS": "bsmith@work.com"}
    flags = -1
    actual = g2_engine.search_by_attributes_v2(json_data, flags)
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(search_schema) == actual_dict


def test_search_by_attributes_v3(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().search_by_attributes_v3()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
        ("CUSTOMERS", "1003"),
    ]
    add_records(g2_engine, test_records)
    # TODO: Uncomment after V3 is published.
    # json_data = {"NAME_FULL": "BOB SMITH", "EMAIL_ADDRESS": "bsmith@work.com"}
    # search_profile = {}
    # flags = -1
    # actual = g2_engine.search_by_attributes_v3(json_data, search_profile, flags)
    delete_records(g2_engine, test_records)
    # actual_dict = json.loads(actual)
    # assert schema(search_schema) == actual_dict


def test_stats(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().stats()."""
    actual = g2_engine.stats()
    actual_dict = json.loads(actual)
    assert schema(stats_schema) == actual_dict


def test_why_entities(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().why_entities()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
    ]
    add_records(g2_engine, test_records)
    entity_id_1 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    entity_id_2 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1002")
    actual = g2_engine.why_entities(entity_id_1, entity_id_2)
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(why_entities_results_schema) == actual_dict


def test_why_entities_v2(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().why_entities_v2()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
    ]
    add_records(g2_engine, test_records)
    entity_id_1 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    entity_id_2 = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1002")
    flags = -1
    actual = g2_engine.why_entities_v2(entity_id_1, entity_id_2, flags)
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(why_entities_results_schema) == actual_dict


def test_why_entity_by_entity_id(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().why_entity_by_entity_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
    ]
    add_records(g2_engine, test_records)
    entity_id = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    actual = g2_engine.why_entity_by_entity_id(entity_id)
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(why_entity_results_schema) == actual_dict


def test_why_entity_by_entity_id_v2(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().why_entity_by_entity_id_v2()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
    ]
    add_records(g2_engine, test_records)
    entity_id = get_entity_id_from_record_id(g2_engine, "CUSTOMERS", "1001")
    flags = -1
    actual = g2_engine.why_entity_by_entity_id_v2(entity_id, flags)
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(why_entity_results_schema) == actual_dict


def test_why_entity_by_record_id(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().why_entity_by_record_id()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
    ]
    add_records(g2_engine, test_records)
    actual = g2_engine.why_entity_by_record_id("CUSTOMERS", "1001")
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(why_entity_results_schema) == actual_dict


def test_why_entity_by_record_id_v2(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().why_entity_by_record_id_v2()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
    ]
    add_records(g2_engine, test_records)
    flags = -1
    actual = g2_engine.why_entity_by_record_id_v2("CUSTOMERS", "1001", flags)
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(why_entity_results_schema) == actual_dict


def test_why_record_in_entity(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().why_record_in_entity()."""
    pass


def test_why_record_in_entity_v2(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().why_record_in_entity_v2()."""
    pass


def test_why_records(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().why_records()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
    ]
    add_records(g2_engine, test_records)
    actual = g2_engine.why_records("CUSTOMERS", "1001", "CUSTOMERS", "1002")
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(why_entity_results_schema) == actual_dict


def test_why_records_v2(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().why_records_v2()."""
    test_records: List[Tuple[str, str]] = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
    ]
    add_records(g2_engine, test_records)
    flags = -1
    actual = g2_engine.why_records_v2("CUSTOMERS", "1001", "CUSTOMERS", "1002", flags)
    delete_records(g2_engine, test_records)
    actual_dict = json.loads(actual)
    assert schema(why_entity_results_schema) == actual_dict


# -----------------------------------------------------------------------------
# G2Engine misc tests
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


# -----------------------------------------------------------------------------
# G2Engine post tests
# -----------------------------------------------------------------------------


def test_destroy(
    g2_engine: g2engine_grpc.G2EngineGrpc,
) -> None:
    """Test G2Engine().destroy()."""
    g2_engine.destroy()
