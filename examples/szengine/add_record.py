#! /usr/bin/env python3


import grpc

from senzing_grpc import SzAbstractFactory, SzEngineFlags, SzError

DATA_SOURCE_CODE = "TEST"
FLAGS = SzEngineFlags.SZ_WITH_INFO
RECORD_DEFINITION = "{}"
RECORD_ID = "1"

try:
    sz_abstract_factory = SzAbstractFactory(
        grpc_channel=grpc.insecure_channel("localhost:8261")
    )
    sz_engine = sz_abstract_factory.create_sz_engine()
    RESULT = sz_engine.add_record(DATA_SOURCE_CODE, RECORD_ID, RECORD_DEFINITION, FLAGS)
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
