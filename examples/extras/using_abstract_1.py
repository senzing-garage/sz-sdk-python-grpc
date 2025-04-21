import grpc
from senzing import SzError
from using_abstract_2 import try_using_abstract

from senzing_grpc import SzAbstractFactoryGrpc, SzAbstractFactoryParametersGrpc

factory_parameters: SzAbstractFactoryParametersGrpc = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}

try:
    sz_abstract_factory = SzAbstractFactoryGrpc(**factory_parameters)
    try_using_abstract(sz_abstract_factory)
except SzError as err:
    print(f"\nERROR: {err}\n")
