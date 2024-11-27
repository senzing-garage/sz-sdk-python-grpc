#! /usr/bin/env python3

import grpc

from senzing_grpc import SzAbstractFactory, SzAbstractFactoryParameters, SzError

CONFIG_COMMENT = "Just an empty example"
FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_config = sz_abstract_factory.create_config()
    sz_configmanager = sz_abstract_factory.create_configmanager()
    config_handle = sz_config.create_config()
    CONFIG_DEFINITION = sz_config.export_config(config_handle)
    config_id = sz_configmanager.add_config(CONFIG_DEFINITION, CONFIG_COMMENT)
except SzError as err:
    print(f"\nError in {__file__}:\n{err}\n")
