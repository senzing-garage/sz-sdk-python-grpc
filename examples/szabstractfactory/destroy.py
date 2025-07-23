import grpc
from senzing import SzError

from senzing_grpc import SzAbstractFactoryGrpc

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_diagnostic = sz_abstract_factory.create_diagnostic()

    # Do work...
except SzError as err:
    print(f"\nERROR: {err}\n")
finally:
    # Destroys the abstract factory and all objects it created, such as sz_engine and sz_diagnostic above
    # If sz_abstract_factory goes out of scope destroy() is automatically called
    sz_abstract_factory.destroy()
