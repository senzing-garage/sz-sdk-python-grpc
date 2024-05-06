#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngine, SzEngineFlags, SzError

END_DATA_SOURCE_CODE = "CUSTOMERS"
END_RECORD_ID = "1009"
EXCLUSIONS = ""
FLAGS = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS
GRPC_URL = "localhost:8261"
MAX_DEGREES = 2
REQUIRED_DATA_SOURCES = ""
START_DATA_SOURCE_CODE = "CUSTOMERS"
START_RECORD_ID = "1001"

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = SzEngine(grpc_channel=grpc_channel)
    RESULT = sz_engine.find_path_by_record_id(
        START_DATA_SOURCE_CODE,
        START_RECORD_ID,
        END_DATA_SOURCE_CODE,
        END_RECORD_ID,
        MAX_DEGREES,
        EXCLUSIONS,
        REQUIRED_DATA_SOURCES,
        FLAGS,
    )
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
