#! /usr/bin/env python3

import grpc

from senzing_grpc import G2Exception, g2configmgr_grpc

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    g2_configmgr = g2configmgr_grpc.SzConfigManagerGrpc(grpc_channel=grpc_channel)

    # Do work.

    g2_configmgr.destroy()
except G2Exception as err:
    print(f"\nError:\n{err}\n")
