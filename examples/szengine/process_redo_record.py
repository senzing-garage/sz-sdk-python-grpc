#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngine, SzEngineFlags, SzError

FLAGS = SzEngineFlags.SZ_WITH_INFO
GRPC_URL = "localhost:8261"

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = SzEngine(grpc_channel=grpc_channel)
    while sz_engine.count_redo_records() > 0:
        REDO_RECORD = sz_engine.get_redo_record()
        RESULT = sz_engine.process_redo_record(REDO_RECORD, FLAGS)
        # TODO: Review this output
        print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
