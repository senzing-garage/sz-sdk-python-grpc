#! /usr/bin/env python3

import grpc

from senzing_grpc import SzAbstractFactory, SzAbstractFactoryParameters, SzError

FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_configmanager = sz_abstract_factory.create_configmanager()
    CONFIG_LIST = sz_configmanager.get_configs()
    print(f"\nFile {__file__}:\n{CONFIG_LIST}\n")
except SzError as err:
    print(f"\nError in {__file__}:\n{err}\n")
