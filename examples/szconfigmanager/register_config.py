import grpc
from senzing import SzError

from senzing_grpc import SzAbstractFactoryGrpc

config_comment = "Just an empty example"

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_configmanager = sz_abstract_factory.create_configmanager()
    sz_config = sz_configmanager.create_config_from_template()
    config_definition = sz_config.export()
    config_id = sz_configmanager.register_config(config_definition, config_comment)
except SzError as err:
    print(f"\nERROR: {err}\n")
