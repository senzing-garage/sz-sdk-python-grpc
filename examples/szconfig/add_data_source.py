#! /usr/bin/env python3

import grpc
from senzing import SzError

from senzing_grpc import SzAbstractFactoryGrpc, SzAbstractFactoryParametersGrpc

DATA_SOURCE_CODE = "NAME_OF_DATASOURCE"
FACTORY_PARAMETERS: SzAbstractFactoryParametersGrpc = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}

try:
    sz_abstract_factory = SzAbstractFactoryGrpc(**FACTORY_PARAMETERS)
    sz_config = sz_abstract_factory.create_config()
    config_handle = sz_config.create_config()
    RESULT = sz_config.add_data_source(config_handle, DATA_SOURCE_CODE)
    sz_config.close_config(config_handle)
    print(f"\nFile {__file__}:\n{RESULT}\n")
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
