#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngine, SzError

GRPC_URL = "localhost:8261"

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = SzEngine(grpc_channel=grpc_channel)
    RESULT = sz_engine.get_active_config_id()
    print(RESULT)
except SzError as err:
    print(f"\nError:\n{err}\n")
