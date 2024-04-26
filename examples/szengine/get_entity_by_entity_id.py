#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngineFlags, SzError, szengine_grpc

GRPC_URL = "localhost:8261"
entity_id = 1
flags = SzEngineFlags.SZ_ENTITY_DEFAULT_FLAGS

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = szengine_grpc.SzEngineGrpc(grpc_channel=grpc_channel)
    RESULT = sz_engine.get_entity_by_entity_id(entity_id, flags)
    print(RESULT)
except SzError as err:
    print(f"\nError:\n{err}\n")
