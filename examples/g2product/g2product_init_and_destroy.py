#! /usr/bin/env python3

import grpc

from senzing_grpc import G2Exception, g2product_grpc

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    g2_product = g2product_grpc.SzProductGrpc(grpc_channel=grpc_channel)

    # Do work.

    g2_product.destroy()
except G2Exception as err:
    print(f"\nError:\n{err}\n")
