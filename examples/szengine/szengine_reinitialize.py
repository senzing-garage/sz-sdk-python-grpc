#! /usr/bin/env python3

import grpc

from senzing_grpc import SzError, szconfigmanager_grpc, szengine_grpc

GRPC_URL = "localhost:8261"
config_id = 1234578

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)

    # Get current default configuration id.

    sz_configmanager = szconfigmanager_grpc.SzConfigManagerGrpc(
        grpc_channel=grpc_channel
    )
    config_id = sz_configmanager.get_default_config_id()

    # Reinitialize engine to current default configuration ID.

    sz_engine = szengine_grpc.SzEngineGrpc(grpc_channel=grpc_channel)
    sz_engine.reinitialize(config_id)
except SzError as err:
    print(f"\nError:\n{err}\n")
