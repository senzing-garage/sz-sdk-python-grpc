#! /usr/bin/env python3

import grpc

from senzing_grpc import SzAbstractFactory, SzAbstractFactoryParameters, SzError

FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}
SECONDS_TO_RUN = 3

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_diagnostic = sz_abstract_factory.create_sz_diagnostic()
    RESULT = sz_diagnostic.check_datastore_performance(SECONDS_TO_RUN)
    print(f"\nFile {__file__}:\n{RESULT}\n")
except SzError as err:
    print(f"\nError in {__file__}:\n{err}\n")
