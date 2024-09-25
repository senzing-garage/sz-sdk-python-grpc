#! /usr/bin/env python3

import grpc

from senzing_grpc import SzAbstractFactory, SzError

try:
    sz_abstract_factory = SzAbstractFactory(
        grpc_channel=grpc.insecure_channel("localhost:8261")
    )
    sz_configmanager = sz_abstract_factory.create_sz_configmanager()
except SzError as err:
    print(f"\nError:\n{err}\n")