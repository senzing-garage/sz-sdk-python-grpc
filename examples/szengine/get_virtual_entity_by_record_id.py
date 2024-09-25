#! /usr/bin/env python3

import grpc

from senzing_grpc import SzAbstractFactory, SzEngineFlags, SzError

FLAGS = SzEngineFlags.SZ_VIRTUAL_ENTITY_DEFAULT_FLAGS
RECORD_LIST = [
    ("CUSTOMERS", "1001"),
    ("CUSTOMERS", "1002"),
]

try:
    sz_abstract_factory = SzAbstractFactory(
        grpc_channel=grpc.insecure_channel("localhost:8261")
    )
    sz_engine = sz_abstract_factory.create_sz_engine()
    RESULT = sz_engine.get_virtual_entity_by_record_id(RECORD_LIST, FLAGS)
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
