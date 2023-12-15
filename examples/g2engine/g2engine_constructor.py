#! /usr/bin/env python3

import grpc

from senzing_grpc import G2Exception, g2engine_grpc

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    g2_engine = g2engine_grpc.G2EngineGrpc(grpc_channel=grpc_channel)
except G2Exception as err:
    print(f"\nError:\n{err}\n")
