#! /usr/bin/env python3

import json

import grpc
from senzing import SzEngineFlags, SzError

from senzing_grpc import SzAbstractFactoryGrpc

ATTRIBUTES = json.dumps({"NAME_FULL": "BOB SMITH", "EMAIL_ADDRESS": "bsmith@work.com"})
ENTITY_ID = 1
FLAGS = SzEngineFlags.SZ_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS
SEARCH_PROFILE = "SEARCH"

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_engine = sz_abstract_factory.create_engine()
    RESULT = sz_engine.why_search(ATTRIBUTES, ENTITY_ID, FLAGS, SEARCH_PROFILE)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
