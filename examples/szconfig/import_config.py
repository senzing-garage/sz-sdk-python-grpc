#! /usr/bin/env python3

from typing import Any, Dict

import grpc

from senzing_grpc import SzError, szconfig_grpc

# This would be a full Senzing configuration.
config_definition: Dict[str, Any] = {}  # In this example, an exception occurs.

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_config = szconfig_grpc.SzConfigGrpc(grpc_channel=grpc_channel)
    config_handle = sz_config.import_config(config_definition)
except SzError as err:
    print(f"\nError:\n{err}\n")
