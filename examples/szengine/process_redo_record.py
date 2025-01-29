#! /usr/bin/env python3

import grpc
from senzing import SzEngineFlags, SzError

from senzing_grpc import SzAbstractFactoryGrpc

FLAGS = SzEngineFlags.SZ_WITH_INFO

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_engine = sz_abstract_factory.create_engine()
    while True:
        REDO_RECORD = sz_engine.get_redo_record()
        if not REDO_RECORD:
            break
        RESULT = sz_engine.process_redo_record(REDO_RECORD, FLAGS)
        print(RESULT)
except SzError as err:
    print(f"\nERROR: {err}\n")
