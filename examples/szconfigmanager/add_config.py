#! /usr/bin/env python3

import grpc

from senzing_grpc import SzError, szconfig_grpc, szconfigmanager_grpc

CONFIG_COMMENT = "Just an empty example"

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_config = szconfig_grpc.SzConfigGrpc(grpc_channel=grpc_channel)
    sz_configmanager = szconfigmanager_grpc.SzConfigManagerGrpc(
        grpc_channel=grpc_channel
    )
    config_handle = sz_config.create_config()
    CONFIG_DEFINITION = sz_config.export_config(config_handle)
    config_id = sz_configmanager.add_config(CONFIG_DEFINITION, CONFIG_COMMENT)
except SzError as err:
    print(f"\nError:\n{err}\n")
