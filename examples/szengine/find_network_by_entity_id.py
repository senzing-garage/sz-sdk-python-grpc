#! /usr/bin/env python3

import grpc

from senzing_grpc import SzEngineFlags, SzError, szengine_grpc

GRPC_URL = "localhost:8261"
entity_list = {
    "ENTITIES": [
        {"ENTITY_ID": 1},
        {"ENTITY_ID": 200001},
    ]
}
max_degrees = 2
build_out_degree = 1
max_entities = 10
flags = SzEngineFlags.SZ_FIND_NETWORK_DEFAULT_FLAGS

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = szengine_grpc.SzEngineGrpc(grpc_channel=grpc_channel)
    RESULT = sz_engine.find_network_by_entity_id(
        entity_list, max_degrees, build_out_degree, max_entities, flags
    )
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
