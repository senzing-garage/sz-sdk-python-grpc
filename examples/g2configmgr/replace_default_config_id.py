#! /usr/bin/env python3


import time

import grpc

from senzing_grpc import g2config_grpc, g2configmgr_grpc
from senzing_grpc.g2exception import G2Exception

COMMENT = "Just an empty example"

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    g2_config = g2config_grpc.G2ConfigGrpc(grpc_channel=grpc_channel)
    g2_configmgr = g2configmgr_grpc.G2ConfigMgrGrpc(grpc_channel=grpc_channel)
    old_config_id = g2_configmgr.get_default_config_id()

    # Create a new config.

    OLD_JSON_CONFIG = g2_configmgr.get_config(old_config_id)
    config_handle = g2_config.load(OLD_JSON_CONFIG)
    input_json = {"DSRC_CODE": f"REPLACE_DEFAULT_CONFIG_ID_{time.time()}"}
    g2_config.add_data_source(config_handle, input_json)
    NEW_JSON_CONFIG = g2_config.save(config_handle)
    new_config_id = g2_configmgr.add_config(NEW_JSON_CONFIG, "Test")

    # Replace default config id.

    g2_configmgr.replace_default_config_id(old_config_id, new_config_id)
except G2Exception as err:
    print(f"\nError:\n{err}\n")
