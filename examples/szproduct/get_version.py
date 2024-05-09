#! /usr/bin/env python3

import grpc

from senzing_grpc import SzError, SzProduct

GRPC_URL = "localhost:8261"

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_product = SzProduct(grpc_channel=grpc_channel)
    RESULT = sz_product.get_version()
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
