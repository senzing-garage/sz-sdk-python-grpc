#! /usr/bin/env python3

import grpc

from senzing_grpc import SzAbstractFactory, SzEngineFlags, SzError

DATA_SOURCE_CODE = "CUSTOMERS"
FLAGS = SzEngineFlags.SZ_WHY_RECORDS_DEFAULT_FLAGS
RECORD_ID = "1001"

try:
    sz_abstract_factory = SzAbstractFactory(
        grpc_channel=grpc.insecure_channel("localhost:8261")
    )
    sz_engine = sz_abstract_factory.create_sz_engine()
    RESULT = sz_engine.why_record_in_entity(
        DATA_SOURCE_CODE,
        RECORD_ID,
        FLAGS,
    )
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
