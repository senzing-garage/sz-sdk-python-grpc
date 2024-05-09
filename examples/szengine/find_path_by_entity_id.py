#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngine, SzEngineFlags, SzError

END_ENTITY_ID = 100004
EXCLUSIONS = ""
FLAGS = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS
GRPC_URL = "localhost:8261"
MAX_DEGREES = 2
REQUIRED_DATA_SOURCES = ""
START_ENTITY_ID = 1

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = SzEngine(grpc_channel=grpc_channel)
    RESULT = sz_engine.find_path_by_entity_id(
        START_ENTITY_ID,
        END_ENTITY_ID,
        MAX_DEGREES,
        EXCLUSIONS,
        REQUIRED_DATA_SOURCES,
        FLAGS,
    )
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
