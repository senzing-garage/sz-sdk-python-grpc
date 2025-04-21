import grpc
from senzing import SzEngineFlags, SzError

from senzing_grpc import SzAbstractFactoryGrpc

data_source_code_1 = "CUSTOMERS"
data_source_code_2 = "CUSTOMERS"
flags = SzEngineFlags.SZ_WHY_ENTITIES_DEFAULT_FLAGS
record_id_1 = "1001"
record_id_2 = "1002"

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_engine = sz_abstract_factory.create_engine()
    result = sz_engine.why_records(
        data_source_code_1,
        record_id_1,
        data_source_code_2,
        record_id_2,
        flags,
    )
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
