#! /usr/bin/env python3

import grpc

from senzing import g2config_grpc
from senzing.g2exception import G2Exception

input_json = {"DSRC_CODE": "NAME_OF_DATASOURCE"}

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    g2_config = g2config_grpc.G2ConfigGrpc(grpc_channel=grpc_channel)
    config_handle = g2_config.create()
    RESULT = g2_config.add_data_source(config_handle, input_json)
    g2_config.close(config_handle)
    print(RESULT)
except G2Exception as err:
    print(f"\nError:\n{err}\n")
