#! /usr/bin/env python3

from typing import Any, Dict

import grpc

from senzing_grpc import SzEngineFlags, SzError, szengine_grpc

GRPC_URL = "localhost:8261"
data_source_code = "TEST"
record_id = "1"
record_definition: Dict[Any, Any] = {}
flags = SzEngineFlags.SZ_WITH_INFO

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = szengine_grpc.SzEngineGrpc(grpc_channel=grpc_channel)
    RESULT = sz_engine.add_record(data_source_code, record_id, record_definition, flags)
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
