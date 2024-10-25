#! /usr/bin/env python3

import grpc
from senzing_truthset import TRUTHSET_DATASOURCES

from senzing_grpc import SzAbstractFactory, SzAbstractFactoryParameters, SzError

FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_config = sz_abstract_factory.create_sz_config()
    sz_configmanager = sz_abstract_factory.create_sz_configmanager()
    sz_diagnostic = sz_abstract_factory.create_sz_diagnostic()
    sz_engine = sz_abstract_factory.create_sz_engine()

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
    sz_abstract_factory.reinitialize(new_default_config_id)
except SzError as err:
    print(f"\nError in {__file__}:\n{err}\n")
