#! /usr/bin/env python3

import grpc

from senzing_grpc import g2config_grpc
from senzing_grpc.g2exception import G2Exception

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    g2_config = g2config_grpc.G2ConfigGrpc(grpc_channel=grpc_channel)
    config_handle_1 = g2_config.create()  # Create first in-memory.
    JSON_CONFIG = g2_config.save(config_handle_1)  # Save in-memory to string.
    config_handle_2 = g2_config.load(JSON_CONFIG)  # Create second in-memory.
    g2_config.close(config_handle_1)
    g2_config.close(config_handle_2)
except G2Exception as err:
    print(f"\nError:\n{err}\n")
