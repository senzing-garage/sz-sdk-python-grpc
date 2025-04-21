import grpc
from senzing import SzError

from senzing_grpc import SzAbstractFactoryGrpc

data_source_code = "NAME_OF_DATASOURCE"

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_configmanager = sz_abstract_factory.create_configmanager()
    sz_config = sz_configmanager.create_config_from_template()
    result = sz_config.add_data_source(data_source_code)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
