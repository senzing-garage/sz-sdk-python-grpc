#! /usr/bin/env python3

import grpc

from senzing_grpc import SzDiagnostic, SzError

GRPC_URL = "localhost:8261"
SECONDS_TO_RUN = 3

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_diagnostic = SzDiagnostic(grpc_channel=grpc_channel)
    RESULT = sz_diagnostic.check_datastore_performance(SECONDS_TO_RUN)
    print(RESULT[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
