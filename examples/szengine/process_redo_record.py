#! /usr/bin/env python3

import grpc

from senzing_grpc import SzAbstractFactory, SzEngineFlags, SzError

FLAGS = SzEngineFlags.SZ_WITH_INFO

try:
    sz_abstract_factory = SzAbstractFactory(
        grpc_channel=grpc.insecure_channel("localhost:8261")
    )
    sz_engine = sz_abstract_factory.create_sz_engine()
    while sz_engine.count_redo_records() > 0:
        REDO_RECORD = sz_engine.get_redo_record()
        RESULT = sz_engine.process_redo_record(REDO_RECORD, FLAGS)
        # TODO: Review this output
        print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
