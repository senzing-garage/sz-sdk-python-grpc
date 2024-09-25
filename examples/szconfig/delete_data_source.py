#! /usr/bin/env python3

import grpc

from senzing_grpc import SzAbstractFactory, SzError

DATA_SOURCE_CODE = "TEST"

try:
    sz_abstract_factory = SzAbstractFactory(
        grpc_channel=grpc.insecure_channel("localhost:8261")
    )
    sz_config = sz_abstract_factory.create_sz_config()
    config_handle = sz_config.create_config()
    sz_config.delete_data_source(config_handle, DATA_SOURCE_CODE)
    sz_config.close_config(config_handle)
except SzError as err:
    print(f"\nError:\n{err}\n")
