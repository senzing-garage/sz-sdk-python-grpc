#! /usr/bin/env python3

import grpc

from senzing_grpc import (
    SzAbstractFactory,
    SzAbstractFactoryParameters,
    SzEngineFlags,
    SzError,
)

FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}
FLAGS = SzEngineFlags.SZ_WITH_INFO

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_engine = sz_abstract_factory.create_engine()
    while sz_engine.count_redo_records() > 0:
        REDO_RECORD = sz_engine.get_redo_record()
        RESULT = sz_engine.process_redo_record(REDO_RECORD, FLAGS)
        # TODO: Review this output
        print(f"\nFile {__file__}:\n{RESULT}\n")
except SzError as err:
    print(f"\nError in {__file__}:\n{err}\n")
