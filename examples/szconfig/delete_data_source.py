#! /usr/bin/env python3

import grpc

from senzing_grpc import G2Exception, g2config_grpc

input_json = {"DSRC_CODE": "TEST"}

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    g2_config = g2config_grpc.SzConfigGrpc(grpc_channel=grpc_channel)
    config_handle = g2_config.create()
    g2_config.delete_data_source(config_handle, input_json)
    g2_config.close(config_handle)
except G2Exception as err:
    print(f"\nError:\n{err}\n")
