import grpc
from senzing import SzError

from senzing_grpc import SzAbstractFactoryGrpc

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_configmanager = sz_abstract_factory.create_configmanager()
    config_list = sz_configmanager.get_config_registry()
    print(f"\n{config_list}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
