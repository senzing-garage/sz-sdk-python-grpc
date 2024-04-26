#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngineFlags, SzError, szengine_grpc

GRPC_URL = "localhost:8261"
csv_column_list = "RESOLVED_ENTITY_ID,RESOLVED_ENTITY_NAME,RELATED_ENTITY_ID,MATCH_LEVEL,MATCH_KEY,IS_DISCLOSED,IS_AMBIGUOUS,DATA_SOURCE,RECORD_ID,JSON_DATA"
flags = SzEngineFlags.SZ_EXPORT_DEFAULT_FLAGS

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = szengine_grpc.SzEngineGrpc(grpc_channel=grpc_channel)
    export_handle = sz_engine.export_csv_entity_report(csv_column_list, flags)
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
