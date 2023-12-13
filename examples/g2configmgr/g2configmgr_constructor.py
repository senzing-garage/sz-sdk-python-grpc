#! /usr/bin/env python3

import grpc

from senzing import g2configmgr_grpc
from senzing.g2exception import G2Exception

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    g2_configmgr = g2configmgr_grpc.G2ConfigMgrGrpc(grpc_channel=grpc_channel)
except G2Exception as err:
    print(f"\nError:\n{err}\n")
