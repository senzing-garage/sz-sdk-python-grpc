#! /usr/bin/env python3

import grpc
from senzing import SzError

from senzing_grpc import SzAbstractFactoryGrpc

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_diagnostic = sz_abstract_factory.create_diagnostic()
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
