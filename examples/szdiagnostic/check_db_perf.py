#! /usr/bin/env python3

import grpc

from senzing_grpc import G2Exception, g2diagnostic_grpc

SECONDS_TO_RUN = 3

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    g2_diagnostic = g2diagnostic_grpc.G2DiagnosticGrpc(grpc_channel=grpc_channel)
    RESULT = g2_diagnostic.check_db_perf(SECONDS_TO_RUN)
    print(RESULT)
except G2Exception as err:
    print(f"\nError:\n{err}\n")
