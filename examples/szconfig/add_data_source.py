#! /usr/bin/env python3

import grpc

from senzing_grpc import SzError, szconfig_grpc

GRPC_URL = "localhost:8261"
data_source_code = "NAME_OF_DATASOURCE"

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_config = szconfig_grpc.SzConfigGrpc(grpc_channel=grpc_channel)
    config_handle = sz_config.create_config()
    RESULT = sz_config.add_data_source(config_handle, data_source_code)
    sz_config.close_config(config_handle)
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
