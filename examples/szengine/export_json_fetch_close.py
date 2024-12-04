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
FLAGS = SzEngineFlags.SZ_EXPORT_DEFAULT_FLAGS

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_engine = sz_abstract_factory.create_engine()
    export_handle = sz_engine.export_json_entity_report(FLAGS)
    RESULT = ""
    while True:
        FRAGMENT = sz_engine.fetch_next(export_handle)
        if len(FRAGMENT) == 0:
            break
        RESULT += FRAGMENT
    sz_engine.close_export(export_handle)
    print(f"\nFile {__file__}:\n{RESULT}\n")
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
