#! /usr/bin/env python3

import grpc

from senzing_grpc import SzError, szconfigmanager_grpc, szdiagnostic_grpc

ini_params_dict = {
    "PIPELINE": {
        "CONFIGPATH": "/etc/opt/senzing",
        "RESOURCEPATH": "/opt/senzing/g2/resources",
        "SUPPORTPATH": "/opt/senzing/data",
    },
    "SQL": {"CONNECTION": "sqlite3://na:na@/tmp/sqlite/G2C.db"},
}
MODULE_NAME = "Example"

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_configmanager = szconfigmanager_grpc.SzConfigManagerGrpc(
        grpc_channel=grpc_channel
    )
    sz_diagnostic = szdiagnostic_grpc.SzDiagnosticGrpc(grpc_channel=grpc_channel)
    config_id = sz_configmanager.get_default_config_id()
    sz_diagnostic.reinitialize(config_id)
except SzError as err:
    print(f"\nError:\n{err}\n")
