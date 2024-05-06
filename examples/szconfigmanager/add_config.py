#! /usr/bin/env python3

import grpc

from senzing_grpc import SzConfig, SzConfigManager, SzError

CONFIG_COMMENT = "Just an empty example"
GRPC_URL = "localhost:8261"

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_config = SzConfig(grpc_channel=grpc_channel)
    sz_configmanager = SzConfigManager(grpc_channel=grpc_channel)
    config_handle = sz_config.create_config()
    CONFIG_DEFINITION = sz_config.export_config(config_handle)
    config_id = sz_configmanager.add_config(CONFIG_DEFINITION, CONFIG_COMMENT)
except SzError as err:
    print(f"\nError:\n{err}\n")
