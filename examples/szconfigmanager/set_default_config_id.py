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
    sz_configmanager = sz_abstract_factory.create_configmanager()

    # Create a new config.

    sz_config = sz_configmanager.create_config_from_template()
    data_source_code = f"REPLACE_DEFAULT_CONFIG_ID_{time.time()}"
    sz_config.add_data_source(data_source_code)

    # Persist the new config.

    CONFIG_DEFINITION = sz_config.export()
    CONFIG_COMMENT = "Just an example"
    NEW_DEFAULT_CONFIG_ID = sz_configmanager.register_config(CONFIG_DEFINITION, CONFIG_COMMENT)

    # Set default config id.

    sz_configmanager.set_default_config_id(NEW_DEFAULT_CONFIG_ID)

except SzError as err:
    print(f"\nERROR: {err}\n")
