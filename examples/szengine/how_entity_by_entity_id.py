#! /usr/bin/env python3

import grpc
from senzing import SzEngineFlags, SzError

from senzing_grpc import SzAbstractFactoryGrpc

ENTITY_ID = 1
FLAGS = SzEngineFlags.SZ_HOW_ENTITY_DEFAULT_FLAGS

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_engine = sz_abstract_factory.create_engine()
    RESULT = sz_engine.how_entity_by_entity_id(ENTITY_ID, FLAGS)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
