#! /usr/bin/env python3

from typing import Any, Dict

import grpc

from senzing_grpc import G2Exception, g2config_grpc

# This would be a full Senzing configuration.
json_config: Dict[str, Any] = {}  # In this example, an exception occurs.

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    g2_config = g2config_grpc.G2ConfigGrpc(grpc_channel=grpc_channel)
    config_handle = g2_config.load(json_config)
except G2Exception as err:
    print(f"\nError:\n{err}\n")
