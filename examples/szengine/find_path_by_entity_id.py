#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngineFlags, SzError, szengine_grpc

GRPC_URL = "localhost:8261"
start_entity_id = 1
end_entity_id = 200001
max_degrees = 2
exclusions = ""
required_data_sources = ""
flags = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = szengine_grpc.SzEngineGrpc(grpc_channel=grpc_channel)
    RESULT = sz_engine.find_path_by_entity_id(
        start_entity_id,
        end_entity_id,
        max_degrees,
        exclusions,
        required_data_sources,
        flags,
    )
    print(RESULT)
except SzError as err:
    print(f"\nError:\n{err}\n")
