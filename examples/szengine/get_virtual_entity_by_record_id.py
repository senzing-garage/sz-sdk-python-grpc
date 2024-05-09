#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngine, SzEngineFlags, SzError

FLAGS = SzEngineFlags.SZ_VIRTUAL_ENTITY_DEFAULT_FLAGS
GRPC_URL = "localhost:8261"
RECORD_LIST = {
    "RECORDS": [
        {"DATA_SOURCE": "CUSTOMERS", "RECORD_ID": "1001"},
        {"DATA_SOURCE": "CUSTOMERS", "RECORD_ID": "1002"},
    ]
}

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = SzEngine(grpc_channel=grpc_channel)
    RESULT = sz_engine.get_virtual_entity_by_record_id(RECORD_LIST, FLAGS)
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
