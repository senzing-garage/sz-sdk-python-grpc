import grpc
from senzing import SzEngineFlags, SzError

from senzing_grpc import SzAbstractFactoryGrpc

data_source_code = "CUSTOMERS"
flags = SzEngineFlags.SZ_WHY_RECORD_IN_ENTITY_DEFAULT_FLAGS
record_id = "1001"

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_engine = sz_abstract_factory.create_engine()
    result = sz_engine.why_record_in_entity(
        data_source_code,
        record_id,
        flags,
    )
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
