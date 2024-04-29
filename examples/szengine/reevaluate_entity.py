#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngineFlags, SzError, szengine_grpc

GRPC_URL = "localhost:8261"
entity_id = 1
flags = SzEngineFlags.SZ_WITH_INFO

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = szengine_grpc.SzEngineGrpc(grpc_channel=grpc_channel)
    RESULT = sz_engine.reevaluate_entity(entity_id, flags)
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
