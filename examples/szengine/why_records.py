#! /usr/bin/env python3

import grpc

from senzing_grpc import SzAbstractFactory, SzEngineFlags, SzError

DATA_SOURCE_CODE_1 = "CUSTOMERS"
DATA_SOURCE_CODE_2 = "CUSTOMERS"
FLAGS = SzEngineFlags.SZ_WHY_ENTITIES_DEFAULT_FLAGS
RECORD_ID_1 = "1001"
RECORD_ID_2 = "1002"

try:
    sz_abstract_factory = SzAbstractFactory(
        grpc_channel=grpc.insecure_channel("localhost:8261")
    )
    sz_engine = sz_abstract_factory.create_sz_engine()
    RESULT = sz_engine.why_records(
        DATA_SOURCE_CODE_1,
        RECORD_ID_1,
        DATA_SOURCE_CODE_2,
        RECORD_ID_2,
        FLAGS,
    )
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
