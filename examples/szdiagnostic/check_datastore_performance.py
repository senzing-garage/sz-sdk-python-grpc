import grpc
from senzing import SzError

from senzing_grpc import SzAbstractFactoryGrpc

seconds_to_run = 3

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_diagnostic = sz_abstract_factory.create_diagnostic()
    result = sz_diagnostic.check_datastore_performance(seconds_to_run)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
