#! /usr/bin/env python3

import time

import grpc
from senzing import SzError

from senzing_grpc import SzAbstractFactoryGrpc, SzAbstractFactoryParametersGrpc

CONFIG_COMMENT = "Just an example"
DATA_SOURCE_CODE = f"REPLACE_DEFAULT_CONFIG_ID_{time.time()}"
FACTORY_PARAMETERS: SzAbstractFactoryParametersGrpc = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}

try:
    sz_abstract_factory = SzAbstractFactoryGrpc(**FACTORY_PARAMETERS)
    sz_config = sz_abstract_factory.create_config()
    sz_configmanager = sz_abstract_factory.create_configmanager()
    old_config_id = sz_configmanager.get_default_config_id()

    # Create a new config.

    OLD_CONFIG_DEFINITION = sz_configmanager.get_config(old_config_id)
    old_config_handle = sz_config.import_config(OLD_CONFIG_DEFINITION)
    sz_config.add_data_source(old_config_handle, DATA_SOURCE_CODE)
    NEW_CONFIG_DEFINITION = sz_config.export_config(old_config_handle)
    config_id = sz_configmanager.add_config(NEW_CONFIG_DEFINITION, CONFIG_COMMENT)

    # Set default config id.

    sz_configmanager.set_default_config_id(config_id)
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
