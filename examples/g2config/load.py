#! /usr/bin/env python3

import json
from typing import Any, Dict

import grpc

from senzing import g2config_grpc
from senzing.g2exception import G2Exception

json_config_dict: Dict[
    str, Any
] = {}  # Naturally, this would be a full Senzing configuration.

try:
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    g2_config = g2config_grpc.G2ConfigGrpc(grpc_channel=grpc_channel)
    config_handle = g2_config.load(json.dumps(json_config_dict))
except G2Exception as err:
    print(err)
