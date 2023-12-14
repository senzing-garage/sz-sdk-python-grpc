#! /usr/bin/env python3

import grpc

from senzing import g2configmgr_grpc, g2diagnostic_grpc
from senzing.g2exception import G2Exception

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
    g2_configmgr = g2configmgr_grpc.G2ConfigMgrGrpc(grpc_channel=grpc_channel)
    g2_diagnostic = g2diagnostic_grpc.G2DiagnosticGrpc(grpc_channel=grpc_channel)
    config_id = g2_configmgr.get_default_config_id()
    g2_diagnostic.reinit(config_id)
except G2Exception as err:
    print(f"\nError:\n{err}\n")
