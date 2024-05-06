#! /usr/bin/env python3


import grpc

from senzing_grpc import SzConfig, SzConfigManager, SzError

GRPC_URL = "localhost:8261"

try:
    # For this example, get default configuration.

    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_configmanager = SzConfigManager(grpc_channel=grpc_channel)
    config_id = sz_configmanager.get_default_config_id()
    CONFIG_DEFINITION = sz_configmanager.get_config(config_id)

    # Import the configuration.

    sz_config = SzConfig(grpc_channel=grpc_channel)
    config_handle = sz_config.import_config(CONFIG_DEFINITION)
except SzError as err:
    print(f"\nError:\n{err}\n")
