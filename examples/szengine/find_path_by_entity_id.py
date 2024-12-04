#! /usr/bin/env python3

from typing import List

import grpc

from senzing_grpc import (
    SzAbstractFactory,
    SzAbstractFactoryParameters,
    SzEngineFlags,
    SzError,
)

AVOID_ENTITY_IDS: List[int] = []
END_ENTITY_ID = 4
FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}
FLAGS = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS
MAX_DEGREES = 2
REQUIRED_DATA_SOURCES: List[str] = []
START_ENTITY_ID = 1

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_engine = sz_abstract_factory.create_engine()
    RESULT = sz_engine.find_path_by_entity_id(
        START_ENTITY_ID,
        END_ENTITY_ID,
        MAX_DEGREES,
        AVOID_ENTITY_IDS,
        REQUIRED_DATA_SOURCES,
        FLAGS,
    )
    print(f"\nFile {__file__}:\n{RESULT}\n")
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
