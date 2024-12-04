#! /usr/bin/env python3

from typing import List, Tuple

import grpc

from senzing_grpc import (
    SzAbstractFactory,
    SzAbstractFactoryParameters,
    SzEngineFlags,
    SzError,
)

AVOID_RECORD_KEYS: List[Tuple[str, str]] = []
END_DATA_SOURCE_CODE = "CUSTOMERS"
END_RECORD_ID = "1009"
FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}
FLAGS = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS
MAX_DEGREES = 2
REQUIRED_DATA_SOURCES: List[str] = []
START_DATA_SOURCE_CODE = "CUSTOMERS"
START_RECORD_ID = "1001"

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_engine = sz_abstract_factory.create_engine()
    RESULT = sz_engine.find_path_by_record_id(
        START_DATA_SOURCE_CODE,
        START_RECORD_ID,
        END_DATA_SOURCE_CODE,
        END_RECORD_ID,
        MAX_DEGREES,
        AVOID_RECORD_KEYS,
        REQUIRED_DATA_SOURCES,
        FLAGS,
    )
    print(f"\nFile {__file__}:\n{RESULT}\n")
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
