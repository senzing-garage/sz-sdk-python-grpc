#! /usr/bin/env python3

import time

import grpc
from senzing import SzError

from senzing_grpc import SzAbstractFactoryGrpc

CONFIG_COMMENT = "Just an example"
DATA_SOURCE_CODE = f"REPLACE_DEFAULT_CONFIG_ID_{time.time()}"

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_config = sz_abstract_factory.create_config()
    sz_configmanager = sz_abstract_factory.create_configmanager()
    current_default_config_id = sz_configmanager.get_default_config_id()

    # Create a new config.

    CURRENT_CONFIG_DEFINITION = sz_configmanager.get_config(current_default_config_id)
    current_config_handle = sz_config.import_config(CURRENT_CONFIG_DEFINITION)
    sz_config.add_data_source(current_config_handle, DATA_SOURCE_CODE)
    NEW_CONFIG_DEFINITION = sz_config.export_config(current_config_handle)
    new_default_config_id = sz_configmanager.add_config(NEW_CONFIG_DEFINITION, CONFIG_COMMENT)

    # Replace default config id.

    sz_configmanager.replace_default_config_id(current_default_config_id, new_default_config_id)
except SzError as err:
    print(f"\nERROR: {err}\n")
