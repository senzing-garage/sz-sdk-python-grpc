#! /usr/bin/env python3

import grpc
from senzing import SzEngineFlags, SzError

from senzing_grpc import SzAbstractFactoryGrpc

CSV_COLUMN_LIST = (
    "RESOLVED_ENTITY_ID,RELATED_ENTITY_ID,RESOLVED_ENTITY_NAME,MATCH_LEVEL,MATCH_KEY,DATA_SOURCE,RECORD_ID"
)
FLAGS = SzEngineFlags.SZ_EXPORT_DEFAULT_FLAGS

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_engine = sz_abstract_factory.create_engine()
    export_handle = sz_engine.export_csv_entity_report(CSV_COLUMN_LIST, FLAGS)
    while True:
        fragment = sz_engine.fetch_next(export_handle)
        if not fragment:
            break
        print(fragment, end="")
    sz_engine.close_export(export_handle)
except SzError as err:
    print(f"\nERROR: {err}\n")
