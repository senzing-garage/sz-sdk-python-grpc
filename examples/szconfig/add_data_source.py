#! /usr/bin/env python3

import grpc
from senzing import SzError

from senzing_grpc import SzAbstractFactoryGrpc

DATA_SOURCE_CODE = "NAME_OF_DATASOURCE"

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_configmanager = sz_abstract_factory.create_configmanager()
    DATA_SOURCE_CODE = "NAME_OF_DATASOURCE"
    sz_config = sz_configmanager.create_config_from_template()
    RESULT = sz_config.add_data_source(DATA_SOURCE_CODE)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
