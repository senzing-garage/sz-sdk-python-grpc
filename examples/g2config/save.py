#! /usr/bin/env python3

import grpc

from senzing_grpc import G2Exception, g2config_grpc

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    g2_config = g2config_grpc.G2ConfigGrpc(grpc_channel=grpc_channel)
    config_handle = g2_config.create()  # Create first in-memory.
    JSON_CONFIG = g2_config.save(config_handle)  # Save in-memory to string.
    g2_config.close(config_handle)
    print(JSON_CONFIG[:66], "...")
except G2Exception as err:
    print(f"\nError:\n{err}\n")
