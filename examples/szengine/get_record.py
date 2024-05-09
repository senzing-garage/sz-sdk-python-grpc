#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngine, SzEngineFlags, SzError

DATA_SOURCE_CODE = "CUSTOMERS"
FLAGS = SzEngineFlags.SZ_RECORD_DEFAULT_FLAGS
GRPC_URL = "localhost:8261"
RECORD_ID = "1001"

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = SzEngine(grpc_channel=grpc_channel)
    RESULT = sz_engine.get_record(DATA_SOURCE_CODE, RECORD_ID, FLAGS)
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
