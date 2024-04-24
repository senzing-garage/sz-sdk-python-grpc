#! /usr/bin/env python3

import grpc

from senzing_grpc import SzError, szconfig_grpc

data_source_code = "TEST"

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_config = szconfig_grpc.SzConfigGrpc(grpc_channel=grpc_channel)
    config_handle = sz_config.create_config()
    sz_config.delete_data_source(config_handle, data_source_code)
    sz_config.close_config(config_handle)
except SzError as err:
    print(f"\nError:\n{err}\n")
