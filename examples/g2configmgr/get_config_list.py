#! /usr/bin/env python3

import grpc

from senzing_grpc import G2Exception, g2configmgr_grpc

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    g2_configmgr = g2configmgr_grpc.SzConfigManagerGrpc(grpc_channel=grpc_channel)
    CONFIG_LIST = g2_configmgr.get_config_list()
    print(CONFIG_LIST[:66], "...")
except G2Exception as err:
    print(f"\nError:\n{err}\n")
