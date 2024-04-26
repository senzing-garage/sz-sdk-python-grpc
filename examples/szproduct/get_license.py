#! /usr/bin/env python3

import grpc

from senzing_grpc import SzError, szproduct_grpc

GRPC_URL = "localhost:8261"

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_product = szproduct_grpc.SzProductGrpc(grpc_channel=grpc_channel)
    RESULT = sz_product.get_license()
    print(RESULT)
except SzError as err:
    print(f"\nError:\n{err}\n")
