#! /usr/bin/env python3

import json

import grpc

from senzing import g2config_grpc
from senzing.g2exception import G2Exception

input_json_dict = {"DSRC_CODE": "NAME_OF_DATASOURCE"}

try:
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    g2_config = g2config_grpc.G2ConfigGrpc(grpc_channel=grpc_channel)
    config_handle = g2_config.create()
    result = g2_config.add_data_source(config_handle, json.dumps(input_json_dict))
    g2_config.close(config_handle)
    print(result)
except G2Exception as err:
    print(err)
