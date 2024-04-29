#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngineFlags, SzError, szengine_grpc

GRPC_URL = "localhost:8261"
attributes = {"NAME_FULL": "BOB SMITH", "EMAIL_ADDRESS": "bsmith@work.com"}
search_profile = "{}"
flags = SzEngineFlags.SZ_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = szengine_grpc.SzEngineGrpc(grpc_channel=grpc_channel)
    RESULT = sz_engine.search_by_attributes(attributes, search_profile, flags)
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
