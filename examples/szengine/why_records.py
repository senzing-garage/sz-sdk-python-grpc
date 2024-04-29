#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngineFlags, SzError, szengine_grpc

GRPC_URL = "localhost:8261"
data_source_code_1 = "CUSTOMERS"
record_id_1 = "1001"
data_source_code_2 = "CUSTOMERS"
record_id_2 = "1002"
flags = SzEngineFlags.SZ_WHY_ENTITIES_DEFAULT_FLAGS

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = szengine_grpc.SzEngineGrpc(grpc_channel=grpc_channel)
    RESULT = sz_engine.why_records(
        data_source_code_1,
        record_id_1,
        data_source_code_2,
        record_id_2,
        flags,
    )
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
