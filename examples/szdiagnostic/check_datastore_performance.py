#! /usr/bin/env python3

import grpc

from senzing_grpc import SzAbstractFactory, SzError

SECONDS_TO_RUN = 3

try:
    sz_abstract_factory = SzAbstractFactory(
        grpc_channel=grpc.insecure_channel("localhost:8261")
    )
    sz_diagnostic = sz_abstract_factory.create_sz_diagnostic()
    RESULT = sz_diagnostic.check_datastore_performance(SECONDS_TO_RUN)
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
