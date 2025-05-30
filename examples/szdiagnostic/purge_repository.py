import grpc
from senzing import SzError

from senzing_grpc import SzAbstractFactoryGrpc

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_diagnostic = sz_abstract_factory.create_diagnostic()
    # WARNING
    # WARNING - This will remove all loaded and entity resolved data from the Senzing repository, use with caution!
    # WARNING - Uncomment the purge_repository() call below to complete a purge
    # WARNING

    # sz_diagnostic.purge_repository()
except SzError as err:
    print(f"\nERROR: {err}\n")
