#! /usr/bin/env python3

import grpc

from senzing_grpc import SzAbstractFactory, SzError

try:
    # Using get_active_config_id for demonstrations purposes
    sz_abstract_factory = SzAbstractFactory(
        grpc_channel=grpc.insecure_channel("localhost:8261")
    )
    sz_engine = sz_abstract_factory.create_sz_engine()
    config_id = sz_engine.get_active_config_id()
    sz_engine.reinitialize(config_id)
except SzError as err:
    print(f"\nError:\n{err}\n")
