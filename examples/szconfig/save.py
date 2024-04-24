#! /usr/bin/env python3

import grpc

from senzing_grpc import SzError, szconfig_grpc

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_config = szconfig_grpc.SzConfigGrpc(grpc_channel=grpc_channel)
    config_handle = sz_config.create_config()  # Create first in-memory.
    JSON_CONFIG = sz_config.export_config(config_handle)  # Save in-memory to string.
    sz_config.close_config(config_handle)
    print(JSON_CONFIG[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
