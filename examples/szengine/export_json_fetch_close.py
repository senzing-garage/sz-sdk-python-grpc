#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngineFlags, SzError, szengine_grpc

GRPC_URL = "localhost:8261"
flags = SzEngineFlags.SZ_EXPORT_DEFAULT_FLAGS

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = szengine_grpc.SzEngineGrpc(grpc_channel=grpc_channel)
    export_handle = sz_engine.export_json_entity_report(flags)
    RESULT = ""
    while True:
        fragment = sz_engine.fetch_next(export_handle)
        if len(fragment) == 0:
            break
        RESULT += fragment
    sz_engine.close_export(export_handle)
    print(RESULT)
except SzError as err:
    print(f"\nError:\n{err}\n")
