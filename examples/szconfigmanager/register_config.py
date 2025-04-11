#! /usr/bin/env python3

import grpc
from senzing import SzError

from senzing_grpc import SzAbstractFactoryGrpc

CONFIG_COMMENT = "Just an empty example"

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_configmanager = sz_abstract_factory.create_configmanager()
    CONFIG_COMMENT = "Just an empty example"
    sz_config = sz_configmanager.create_config_from_template()
    CONFIG_DEFINITION = sz_config.export()
    CONFIG_ID = sz_configmanager.register_config(CONFIG_DEFINITION, CONFIG_COMMENT)
except SzError as err:
    print(f"\nERROR: {err}\n")
