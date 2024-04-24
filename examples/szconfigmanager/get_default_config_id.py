#! /usr/bin/env python3

import grpc

from senzing_grpc import SzError, szconfigmanager_grpc

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_configmanager = szconfigmanager_grpc.SzConfigManagerGrpc(
        grpc_channel=grpc_channel
    )
    config_id = sz_configmanager.get_default_config_id()
except SzError as err:
    print(f"\nError:\n{err}\n")
