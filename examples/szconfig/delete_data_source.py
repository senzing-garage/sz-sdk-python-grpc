#! /usr/bin/env python3

import grpc

from senzing_grpc import SzAbstractFactory, SzAbstractFactoryParameters, SzError

DATA_SOURCE_CODE = "TEST"
FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_config = sz_abstract_factory.create_sz_config()
    config_handle = sz_config.create_config()
    sz_config.delete_data_source(config_handle, DATA_SOURCE_CODE)
    sz_config.close_config(config_handle)
except SzError as err:
    print(f"\nError in {__file__}:\n{err}\n")
