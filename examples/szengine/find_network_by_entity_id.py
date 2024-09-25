#! /usr/bin/env python3

import grpc

from senzing_grpc import SzAbstractFactory, SzEngineFlags, SzError

BUILD_OUT_DEGREE = 1
ENTITY_LIST = [1, 100004]
FLAGS = SzEngineFlags.SZ_FIND_NETWORK_DEFAULT_FLAGS
MAX_DEGREES = 2
MAX_ENTITIES = 10

try:
    sz_abstract_factory = SzAbstractFactory(
        grpc_channel=grpc.insecure_channel("localhost:8261")
    )
    sz_engine = sz_abstract_factory.create_sz_engine()
    RESULT = sz_engine.find_network_by_entity_id(
        ENTITY_LIST, MAX_DEGREES, BUILD_OUT_DEGREE, MAX_ENTITIES, FLAGS
    )
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
