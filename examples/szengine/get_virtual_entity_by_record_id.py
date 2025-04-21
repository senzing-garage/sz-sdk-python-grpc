import grpc
from senzing import SzEngineFlags, SzError

from senzing_grpc import SzAbstractFactoryGrpc

flags = SzEngineFlags.SZ_VIRTUAL_ENTITY_DEFAULT_FLAGS
record_list = [
    ("CUSTOMERS", "1001"),
    ("CUSTOMERS", "1002"),
]

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_engine = sz_abstract_factory.create_engine()
    result = sz_engine.get_virtual_entity_by_record_id(record_list, flags)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
