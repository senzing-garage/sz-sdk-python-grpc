#! /usr/bin/env python3

import grpc
from senzing import SzEngineFlags, SzError

from senzing_grpc import SzAbstractFactoryGrpc, SzAbstractFactoryParametersGrpc

BUILD_OUT_DEGREES = 1
ENTITY_LIST = [1, 4]
FACTORY_PARAMETERS: SzAbstractFactoryParametersGrpc = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}
FLAGS = SzEngineFlags.SZ_FIND_NETWORK_DEFAULT_FLAGS
MAX_DEGREES = 2
MAX_ENTITIES = 10

try:
    sz_abstract_factory = SzAbstractFactoryGrpc(**FACTORY_PARAMETERS)
    sz_engine = sz_abstract_factory.create_engine()
    RESULT = sz_engine.find_network_by_entity_id(ENTITY_LIST, MAX_DEGREES, BUILD_OUT_DEGREES, MAX_ENTITIES, FLAGS)
    print(f"\nFile {__file__}:\n{RESULT}\n")
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
