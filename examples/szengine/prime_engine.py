s  #! /usr/bin/env python3


import grpc

from senzing_grpc import SzError, szengine_grpc

GRPC_URL = "localhost:8261"

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = szengine_grpc.SzEngineGrpc(grpc_channel=grpc_channel)
    RESULT = sz_engine.prime_engine()
    print(RESULT)
except SzError as err:
    print(f"\nError:\n{err}\n")
