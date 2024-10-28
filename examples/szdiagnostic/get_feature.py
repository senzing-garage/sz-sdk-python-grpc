#! /usr/bin/env python3

import grpc

from senzing_grpc import SzAbstractFactory, SzAbstractFactoryParameters, SzError

FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_diagnostic = sz_abstract_factory.create_sz_diagnostic()
    RESULT = sz_diagnostic.get_feature(1)
    print(RESULT)
except SzError as err:
    print(f"\nError:\n{err}\n")
