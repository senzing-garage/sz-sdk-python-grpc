#! /usr/bin/env python3

import grpc

from senzing_grpc import SzError, szdiagnostic_grpc

GRPC_URL = "localhost:8261"

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_diagnostic = szdiagnostic_grpc.SzDiagnosticGrpc(grpc_channel=grpc_channel)
    RESULT = sz_diagnostic.get_datastore_info()
    print(RESULT)
except SzError as err:
    print(f"\nError:\n{err}\n")
