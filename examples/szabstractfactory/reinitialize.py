import grpc
from senzing import SzError

from senzing_grpc import SzAbstractFactoryGrpc

try:
    # Using get_active_config_id for demonstrations purposes.
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_engine = sz_abstract_factory.create_engine()
    config_id = sz_engine.get_active_config_id()
    sz_abstract_factory.reinitialize(config_id)
except SzError as err:
    print(f"\nERROR: {err}\n")
