#! /usr/bin/env python3

import grpc

from senzing import g2config_grpc
from senzing.g2exception import G2Exception

try:
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    g2_config = g2config_grpc.G2ConfigGrpc(grpc_channel=grpc_channel)
    config_handle_1 = g2_config.create()  # Create first in-memory.
    json_config = g2_config.save(config_handle_1)  # Save in-memory to string.
    config_handle_2 = g2_config.load(json_config)  # Create second in-memory.
    g2_config.close(config_handle_1)
    g2_config.close(config_handle_2)
except G2Exception as err:
    print(err)
