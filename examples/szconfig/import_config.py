#! /usr/bin/env python3

import grpc

from senzing_grpc import SzAbstractFactory, SzAbstractFactoryParameters, SzError

FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_config = sz_abstract_factory.create_sz_config()
    sz_configmanager = sz_abstract_factory.create_sz_configmanager()
    config_id = sz_configmanager.get_default_config_id()
    config_definition = sz_configmanager.get_config(config_id)
    config_handle = sz_config.import_config(config_definition)
except SzError as err:
    print(f"\nError in {__file__}:\n{err}\n")
