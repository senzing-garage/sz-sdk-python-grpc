#! /usr/bin/env python3

import grpc

from senzing_grpc import (
    SzAbstractFactory,
    SzAbstractFactoryParameters,
    SzEngineFlags,
    SzError,
)

ENTITY_ID = 1
FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}
FLAGS = SzEngineFlags.SZ_WITH_INFO

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_engine = sz_abstract_factory.create_engine()
    RESULT = sz_engine.reevaluate_entity(ENTITY_ID, FLAGS)
    print(f"\nFile {__file__}:\n{RESULT}\n")
except SzError as err:
    print(f"\nError in {__file__}:\n{err}\n")
