#! /usr/bin/env python3


import grpc

from senzing_grpc import SzError, szconfig_grpc, szconfigmanager_grpc

GRPC_URL = "localhost:8261"

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)

    # For this example, get default configuration.

    sz_configmanager = szconfigmanager_grpc.SzConfigManagerGrpc(
        grpc_channel=grpc_channel
    )
    config_id = sz_configmanager.get_default_config_id()
    config_definition = sz_configmanager.get_config(config_id)

    # Import the configuration.

    sz_config = szconfig_grpc.SzConfigGrpc(grpc_channel=grpc_channel)
    config_handle = sz_config.import_config(config_definition)
except SzError as err:
    print(f"\nError:\n{err}\n")
