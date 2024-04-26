#! /usr/bin/env python3

import time

import grpc

from senzing_grpc import SzError, szconfig_grpc, szconfigmanager_grpc

CONFIG_COMMENT = "Just an example"
data_source_code = f"REPLACE_DEFAULT_CONFIG_ID_{time.time()}"
GRPC_URL = "localhost:8261"

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_config = szconfig_grpc.SzConfigGrpc(grpc_channel=grpc_channel)
    sz_configmanager = szconfigmanager_grpc.SzConfigManagerGrpc(
        grpc_channel=grpc_channel
    )
    old_config_id = sz_configmanager.get_default_config_id()

    # Create a new config.

    OLD_CONFIG_DEFINITION = sz_configmanager.get_config(old_config_id)
    old_config_handle = sz_config.import_config(OLD_CONFIG_DEFINITION)
    sz_config.add_data_source(old_config_handle, data_source_code)
    NEW_CONFIG_DEFINITION = sz_config.export_config(old_config_handle)
    new_config_id = sz_configmanager.add_config(NEW_CONFIG_DEFINITION, CONFIG_COMMENT)

    # Set default config id.

    sz_configmanager.set_default_config_id(new_config_id)
except SzError as err:
    print(f"\nError:\n{err}\n")
