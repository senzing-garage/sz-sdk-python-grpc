#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngineFlags, SzError, szengine_grpc

GRPC_URL = "localhost:8261"
data_source_code = "CUSTOMERS"
record_id = "1001"
flags = SzEngineFlags.SZ_ENTITY_DEFAULT_FLAGS

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = szengine_grpc.SzEngineGrpc(grpc_channel=grpc_channel)
    RESULT = sz_engine.get_entity_by_record_id(data_source_code, record_id, flags)
    print(RESULT)
except SzError as err:
    print(f"\nError:\n{err}\n")
