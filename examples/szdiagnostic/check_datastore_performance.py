#! /usr/bin/env python3

import grpc

from senzing_grpc import SzError, szdiagnostic_grpc

SECONDS_TO_RUN = 3

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_diagnostic = szdiagnostic_grpc.SzDiagnosticGrpc(grpc_channel=grpc_channel)
    RESULT = sz_diagnostic.check_datastore_performance(SECONDS_TO_RUN)
    print(RESULT)
except SzError as err:
    print(f"\nError:\n{err}\n")
