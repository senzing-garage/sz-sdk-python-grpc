#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngine, SzEngineFlags, SzError

BUILD_OUT_DEGREE = 1
FLAGS = SzEngineFlags.SZ_FIND_NETWORK_DEFAULT_FLAGS
GRPC_URL = "localhost:8261"
RECORD_LIST = {
    "RECORDS": [
        {"DATA_SOURCE": "CUSTOMERS", "RECORD_ID": "1001"},
        {"DATA_SOURCE": "CUSTOMERS", "RECORD_ID": "1009"},
    ]
}
MAX_DEGREES = 2
BUILD_OUT_DEGREE = 1
MAX_ENTITIES = 10
FLAGS = SzEngineFlags.SZ_FIND_NETWORK_DEFAULT_FLAGS

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = SzEngine(grpc_channel=grpc_channel)
    RESULT = sz_engine.find_network_by_record_id(
        RECORD_LIST, MAX_DEGREES, BUILD_OUT_DEGREE, MAX_ENTITIES, FLAGS
    )
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
