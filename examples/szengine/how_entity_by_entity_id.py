#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngine, SzEngineFlags, SzError

ENTITY_ID = 1
FLAGS = SzEngineFlags.SZ_HOW_ENTITY_DEFAULT_FLAGS
GRPC_URL = "localhost:8261"

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = SzEngine(grpc_channel=grpc_channel)
    RESULT = sz_engine.how_entity_by_entity_id(ENTITY_ID, FLAGS)
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
