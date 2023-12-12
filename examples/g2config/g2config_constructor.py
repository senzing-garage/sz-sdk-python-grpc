#! /usr/bin/env python3


import grpc

from senzing import g2config_grpc
from senzing.g2exception import G2Exception

# Example 1

try:
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    g2_config = g2config_grpc.G2ConfigGrpc(grpc_channel=grpc_channel)
except G2Exception as err:
    print(err)
