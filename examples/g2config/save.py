#! /usr/bin/env python3

import grpc

from senzing import g2config_grpc
from senzing.g2exception import G2Exception

try:
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    g2_config = g2config_grpc.G2ConfigGrpc(grpc_channel=grpc_channel)
    config_handle = g2_config.create()  # Create first in-memory.
    json_config = g2_config.save(config_handle)  # Save in-memory to string.
    g2_config.close(config_handle)
    print(json_config)
except G2Exception as err:
    print(err)
