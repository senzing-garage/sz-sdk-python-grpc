#! /usr/bin/env python3

import grpc

from senzing_grpc import g2configmgr_grpc
from senzing_grpc.g2exception import G2Exception

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    g2_configmgr = g2configmgr_grpc.G2ConfigMgrGrpc(grpc_channel=grpc_channel)
    config_id = g2_configmgr.get_default_config_id()
    CONFIG_STR = g2_configmgr.get_config(config_id)
    print(CONFIG_STR[:66], "...")
except G2Exception as err:
    print(f"\nError:\n{err}\n")
