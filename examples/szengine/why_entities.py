#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngineFlags, SzError, szengine_grpc

GRPC_URL = "localhost:8261"
entity_id_1 = 1
entity_id_2 = 200001
flags = SzEngineFlags.SZ_WHY_ENTITIES_DEFAULT_FLAGS

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = szengine_grpc.SzEngineGrpc(grpc_channel=grpc_channel)
    RESULT = sz_engine.why_entities(
        entity_id_1,
        entity_id_2,
        flags,
    )
    print(RESULT)
except SzError as err:
    print(f"\nError:\n{err}\n")
