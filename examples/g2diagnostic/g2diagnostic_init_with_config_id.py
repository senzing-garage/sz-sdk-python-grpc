#! /usr/bin/env python3

import grpc

from senzing_grpc import G2Exception, g2configmgr_grpc, g2diagnostic_grpc

try:
    GRPC_URL = "localhost:8261"
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    g2_configmgr = g2configmgr_grpc.SzConfigManagerGrpc(grpc_channel=grpc_channel)
    g2_diagnostic = g2diagnostic_grpc.G2DiagnosticGrpc(grpc_channel=grpc_channel)

    config_id = g2_configmgr.get_default_config_id()

    # TODO:  Figure out what the proper behavior is.
    # g2_diagnostic.init_with_config_id(
    #     MODULE_NAME, json.dumps(ini_params_dict), config_id
    # )
except G2Exception as err:
    print(f"\nError:\n{err}\n")
