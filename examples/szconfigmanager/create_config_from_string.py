import json

import grpc
from senzing import SzError

from senzing_grpc import SzAbstractFactoryGrpc

config_definition = json.dumps({"G2_CONFIG": {}})

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_configmanager = sz_abstract_factory.create_configmanager()
    sz_config = sz_configmanager.create_config_from_string(config_definition)
except SzError as err:
    print(f"\nERROR: {err}\n")
