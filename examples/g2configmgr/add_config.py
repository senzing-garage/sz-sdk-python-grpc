#! /usr/bin/env python3

import grpc

from senzing_grpc import G2Exception, g2config_grpc, g2configmgr_grpc

CONFIG_COMMENTS = "Just an empty example"

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    g2_config = g2config_grpc.G2ConfigGrpc(grpc_channel=grpc_channel)
    g2_configmgr = g2configmgr_grpc.G2ConfigMgrGrpc(grpc_channel=grpc_channel)
    config_handle = g2_config.create()
    CONFIG_STR = g2_config.save(config_handle)
    config_id = g2_configmgr.add_config(CONFIG_STR, CONFIG_COMMENTS)
except G2Exception as err:
    print(f"\nError:\n{err}\n")
