#! /usr/bin/env python3

import grpc
from senzing_truthset import TRUTHSET_DATASOURCES

from senzing_grpc import SzConfig, SzConfigManager, SzDiagnostic, SzEngine, SzError

GRPC_URL = "localhost:8261"

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_config = SzConfig(grpc_channel=grpc_channel)
    sz_configmanager = SzConfigManager(grpc_channel=grpc_channel)
    sz_diagnostic = SzDiagnostic(grpc_channel=grpc_channel)
    sz_engine = SzEngine(grpc_channel=grpc_channel)

    current_default_config_id = sz_configmanager.get_default_config_id()
    OLD_CONFIG_DEFINITION = sz_configmanager.get_config(current_default_config_id)
    config_handle = sz_config.import_config(OLD_CONFIG_DEFINITION)
    for data_source_code in TRUTHSET_DATASOURCES:
        sz_config.add_data_source(config_handle, data_source_code)
    NEW_CONFIG_DEFINITION = sz_config.export_config(config_handle)
    new_default_config_id = sz_configmanager.add_config(
        NEW_CONFIG_DEFINITION, "Add TruthSet datasources"
    )
    sz_configmanager.replace_default_config_id(
        current_default_config_id, new_default_config_id
    )
    sz_engine.reinitialize(new_default_config_id)
    sz_diagnostic.reinitialize(new_default_config_id)
except SzError as err:
    print(f"\nError:\n{err}\n")
