#! /usr/bin/env python3

import grpc

from senzing_grpc import SzAbstractFactory, SzError

try:
    sz_abstract_factory = SzAbstractFactory(
        grpc_channel=grpc.insecure_channel("localhost:8261")
    )
    sz_config = sz_abstract_factory.create_sz_config()
    config_handle_1 = sz_config.create_config()  # Create first in-memory.
    CONFIG_DEFINITION = sz_config.export_config(
        config_handle_1
    )  # Save in-memory to string.
    config_handle_2 = sz_config.import_config(
        CONFIG_DEFINITION
    )  # Create second in-memory.
    sz_config.close_config(config_handle_1)
    sz_config.close_config(config_handle_2)
except SzError as err:
    print(f"\nError:\n{err}\n")
