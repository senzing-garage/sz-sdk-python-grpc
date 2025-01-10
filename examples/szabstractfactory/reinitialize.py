#! /usr/bin/env python3

import grpc
from senzing import SzError

from senzing_grpc import SzAbstractFactoryGrpc, SzAbstractFactoryParametersGrpc

FACTORY_PARAMETERS: SzAbstractFactoryParametersGrpc = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}

try:
    # Using get_active_config_id for demonstrations purposes.
    sz_abstract_factory = SzAbstractFactoryGrpc(**FACTORY_PARAMETERS)
    sz_engine = sz_abstract_factory.create_engine()
    config_id = sz_engine.get_active_config_id()
    sz_abstract_factory.reinitialize(config_id)
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
