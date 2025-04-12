#! /usr/bin/env python3

import json

import grpc
from senzing import SzError

from senzing_grpc import SzAbstractFactoryGrpc

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_configmanager = sz_abstract_factory.create_configmanager()
    CONFIG_DEFINITION = json.dumps({"G2_CONFIG": {}})
    sz_config = sz_configmanager.create_config_from_string(CONFIG_DEFINITION)
except SzError as err:
    print(f"\nERROR: {err}\n")
