#! /usr/bin/env python3

import grpc

from senzing_grpc import SzAbstractFactory, SzEngineFlags, SzError

ENTITY_ID = 1
FLAGS = SzEngineFlags.SZ_HOW_ENTITY_DEFAULT_FLAGS

try:
    sz_abstract_factory = SzAbstractFactory(
        grpc_channel=grpc.insecure_channel("localhost:8261")
    )
    sz_engine = sz_abstract_factory.create_sz_engine()
    RESULT = sz_engine.how_entity_by_entity_id(ENTITY_ID, FLAGS)
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
