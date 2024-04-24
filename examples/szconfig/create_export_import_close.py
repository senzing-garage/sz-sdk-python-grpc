#! /usr/bin/env python3

import grpc

from senzing_grpc import SzError, szconfig_grpc

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_config = szconfig_grpc.SzConfigGrpc(grpc_channel=grpc_channel)
    config_handle_1 = sz_config.create_config()  # Create first in-memory.
    CONFIG_DEFINITION = sz_config.export_config(
        config_handle_1
    )  # Save in-memory to string.
    config_handle_2 = sz_config.import_config(
        CONFIG_DEFINITION
    )  # Create second in-memory.
    sz_config.close_config(config_handle_1)
    sz_config.close_config(config_handle_2)
except SzError as err:
    print(f"\nError:\n{err}\n")
