#! /usr/bin/env python3

import grpc
from senzing import SzError

from senzing_grpc import SzAbstractFactoryGrpc, SzAbstractFactoryParametersGrpc

FACTORY_PARAMETERS: SzAbstractFactoryParametersGrpc = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}

try:
    sz_abstract_factory = SzAbstractFactoryGrpc(**FACTORY_PARAMETERS)
    sz_config = sz_abstract_factory.create_config()
    config_handle_1 = sz_config.create_config()  # Create first in-memory.
    CONFIG_DEFINITION = sz_config.export_config(config_handle_1)  # Save in-memory to string.
    config_handle_2 = sz_config.import_config(CONFIG_DEFINITION)  # Create second in-memory.
    sz_config.close_config(config_handle_1)
    sz_config.close_config(config_handle_2)
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
