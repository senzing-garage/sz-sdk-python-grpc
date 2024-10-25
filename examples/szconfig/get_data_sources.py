#! /usr/bin/env python3

import grpc

from senzing_grpc import SzAbstractFactory, SzAbstractFactoryParameters, SzError

FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_config = sz_abstract_factory.create_sz_config()
    config_handle = sz_config.create_config()
    RESULT = sz_config.get_data_sources(config_handle)
    sz_config.close_config(config_handle)
    print(f"\nFile {__file__}:\n{RESULT}\n")
except SzError as err:
    print(f"\nError in {__file__}:\n{err}\n")
