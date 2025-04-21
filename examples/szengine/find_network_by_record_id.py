import grpc
from senzing import SzEngineFlags, SzError

from senzing_grpc import SzAbstractFactoryGrpc

build_out_degrees = 1
flags = SzEngineFlags.SZ_FIND_NETWORK_DEFAULT_FLAGS
max_degrees = 2
max_entities = 10
record_list = [("CUSTOMERS", "1001"), ("CUSTOMERS", "1009")]

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_engine = sz_abstract_factory.create_engine()
    result = sz_engine.find_network_by_record_id(record_list, max_degrees, build_out_degrees, max_entities, flags)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
