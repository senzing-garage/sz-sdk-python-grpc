#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngineFlags, SzError, szengine_grpc

GRPC_URL = "localhost:8261"
record_list = {
    "RECORDS": [
        {"DATA_SOURCE": "CUSTOMERS", "RECORD_ID": "1001"},
        {"DATA_SOURCE": "CUSTOMERS", "RECORD_ID": "1002"},
    ]
}
max_degrees = 2
build_out_degree = 1
max_entities = 10
flags = SzEngineFlags.SZ_FIND_NETWORK_DEFAULT_FLAGS

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = szengine_grpc.SzEngineGrpc(grpc_channel=grpc_channel)
    RESULT = sz_engine.find_network_by_record_id(
        record_list, max_degrees, build_out_degree, max_entities, flags
    )
    print(RESULT)
except SzError as err:
    print(f"\nError:\n{err}\n")
