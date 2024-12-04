#! /usr/bin/env python3

import grpc

from senzing_grpc import (
    SzAbstractFactory,
    SzAbstractFactoryParameters,
    SzEngineFlags,
    SzError,
)

ENTITY_ID_1 = 1
ENTITY_ID_2 = 4
FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}
FLAGS = SzEngineFlags.SZ_WHY_ENTITIES_DEFAULT_FLAGS

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_engine = sz_abstract_factory.create_engine()
    RESULT = sz_engine.why_entities(
        ENTITY_ID_1,
        ENTITY_ID_2,
        FLAGS,
    )
    print(f"\nFile {__file__}:\n{RESULT}\n")
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
