#! /usr/bin/env python3

import grpc
from senzing import SzError
from using_abstract_2 import try_using_abstract

from senzing_grpc import SzAbstractFactoryGrpc, SzAbstractFactoryParametersGrpc

FACTORY_PARAMETERS: SzAbstractFactoryParametersGrpc = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}

try:
    sz_abstract_factory = SzAbstractFactoryGrpc(**FACTORY_PARAMETERS)
    try_using_abstract(sz_abstract_factory)
except SzError as err:
    print(f"\nERROR: {err}\n")
