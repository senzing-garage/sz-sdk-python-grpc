#! /usr/bin/env python3

import grpc

from senzing_grpc import SzAbstractFactory, SzError

try:
    sz_abstract_factory = SzAbstractFactory(
        grpc_channel=grpc.insecure_channel("localhost:8261")
    )
    sz_config = sz_abstract_factory.create_sz_config()
    config_handle = sz_config.create_config()
    RESULT = sz_config.get_data_sources(config_handle)
    sz_config.close_config(config_handle)
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
