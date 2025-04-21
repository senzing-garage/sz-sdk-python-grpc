import grpc
from senzing import SzEngineFlags, SzError

from senzing_grpc import SzAbstractFactoryGrpc

flags = SzEngineFlags.SZ_WITH_INFO

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_engine = sz_abstract_factory.create_engine()
    while True:
        redo_record = sz_engine.get_redo_record()
        if not redo_record:
            break
        result = sz_engine.process_redo_record(redo_record, flags)
        print(result)
except SzError as err:
    print(f"\nERROR: {err}\n")
