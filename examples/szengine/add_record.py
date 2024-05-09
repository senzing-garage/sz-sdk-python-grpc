#! /usr/bin/env python3

from typing import Any, Dict

import grpc

from senzing_grpc import SzEngine, SzEngineFlags, SzError

DATA_SOURCE_CODE = "TEST"
FLAGS = SzEngineFlags.SZ_WITH_INFO
GRPC_URL = "localhost:8261"
RECORD_DEFINITION: Dict[Any, Any] = {}
RECORD_ID = "1"

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = SzEngine(grpc_channel=grpc_channel)
    RESULT = sz_engine.add_record(DATA_SOURCE_CODE, RECORD_ID, RECORD_DEFINITION, FLAGS)
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
