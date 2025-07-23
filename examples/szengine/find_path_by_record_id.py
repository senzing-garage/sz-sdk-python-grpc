from typing import List, Tuple

import grpc
from senzing import SzEngineFlags, SzError

from senzing_grpc import SzAbstractFactoryGrpc

avoid_record_keys: List[Tuple[str, str]] = []
end_data_source_code = "WATCHLIST"
end_record_id = "1007"
flags = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS
max_degrees = 2
required_data_sources: List[str] = []
start_data_source_code = "CUSTOMERS"
start_record_id = "1001"

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_engine = sz_abstract_factory.create_engine()
    result = sz_engine.find_path_by_record_id(
        start_data_source_code,
        start_record_id,
        end_data_source_code,
        end_record_id,
        max_degrees,
        avoid_record_keys,
        required_data_sources,
        flags,
    )
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
