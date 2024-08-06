#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngine, SzEngineFlags, SzError

BUILD_OUT_DEGREE = 1
FLAGS = SzEngineFlags.SZ_FIND_NETWORK_DEFAULT_FLAGS
GRPC_URL = "localhost:8261"
MAX_DEGREES = 2
MAX_ENTITIES = 10
RECORD_LIST = [("CUSTOMERS", "1001"), ("CUSTOMERS", "1009")]

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = SzEngine(grpc_channel=grpc_channel)
    RESULT = sz_engine.find_network_by_record_id(
        RECORD_LIST, MAX_DEGREES, BUILD_OUT_DEGREE, MAX_ENTITIES, FLAGS
    )
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
