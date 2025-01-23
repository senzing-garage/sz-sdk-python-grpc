#! /usr/bin/env python3

import grpc
from senzing import SzError

from senzing_grpc import SzAbstractFactoryGrpc

DATA_SOURCE_CODE = "TEST"

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_config = sz_abstract_factory.create_config()
    config_handle = sz_config.create_config()
    sz_config.delete_data_source(config_handle, DATA_SOURCE_CODE)
    sz_config.close_config(config_handle)
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
