#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngineFlags, SzError, szengine_grpc

GRPC_URL = "localhost:8261"
start_data_source_code = "CUSTOMERS"
start_record_id = "1001"
end_data_source_code = "CUSTOMERS"
end_record_id = "1002"
max_degrees = 2
exclusions = ""
required_data_sources = ""
flags = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = szengine_grpc.SzEngineGrpc(grpc_channel=grpc_channel)
    RESULT = sz_engine.find_path_by_record_id(
        start_data_source_code,
        start_record_id,
        end_data_source_code,
        end_record_id,
        max_degrees,
        exclusions,
        required_data_sources,
        flags,
    )
    print(RESULT)
except SzError as err:
    print(f"\nError:\n{err}\n")
