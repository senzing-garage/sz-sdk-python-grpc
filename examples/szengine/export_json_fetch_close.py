#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngine, SzEngineFlags, SzError

FLAGS = SzEngineFlags.SZ_EXPORT_DEFAULT_FLAGS
GRPC_URL = "localhost:8261"

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = SzEngine(grpc_channel=grpc_channel)
    export_handle = sz_engine.export_json_entity_report(FLAGS)
    RESULT = ""
    while True:
        FRAGMENT = sz_engine.fetch_next(export_handle)
        if len(FRAGMENT) == 0:
            break
        RESULT += FRAGMENT
    sz_engine.close_export(export_handle)
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
