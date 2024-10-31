#! /usr/bin/env python3

import grpc

from senzing_grpc import (
    SzAbstractFactory,
    SzAbstractFactoryParameters,
    SzEngineFlags,
    SzError,
)

BUILD_OUT_DEGREES = 1
FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}
FLAGS = SzEngineFlags.SZ_FIND_NETWORK_DEFAULT_FLAGS
MAX_DEGREES = 2
MAX_ENTITIES = 10
RECORD_LIST = [("CUSTOMERS", "1001"), ("CUSTOMERS", "1009")]

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_engine = sz_abstract_factory.create_sz_engine()
    RESULT = sz_engine.find_network_by_record_id(RECORD_LIST, MAX_DEGREES, BUILD_OUT_DEGREES, MAX_ENTITIES, FLAGS)
    print(f"\nFile {__file__}:\n{RESULT}\n")
except SzError as err:
    print(f"\nError in {__file__}:\n{err}\n")
