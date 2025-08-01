import time

import grpc
from senzing import SzError

from senzing_grpc import SzAbstractFactoryGrpc

config_comment = "Just an example"
data_source_code = f"REPLACE_DEFAULT_CONFIG_ID_{time.time()}"

try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_configmanager = sz_abstract_factory.create_configmanager()
    sz_config = sz_configmanager.create_config_from_template()
    current_default_config_id = sz_configmanager.get_default_config_id()

    # Create a new config.

    sz_config = sz_configmanager.create_config_from_config_id(current_default_config_id)
    sz_config.register_data_source(data_source_code)

    # Persist the new config.

    config_definition = sz_config.export()
    new_default_config_id = sz_configmanager.register_config(config_definition, config_comment)

    # Replace default config id.

    sz_configmanager.replace_default_config_id(current_default_config_id, new_default_config_id)
except SzError as err:
    print(f"\nERROR: {err}\n")
