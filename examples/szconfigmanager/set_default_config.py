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

    # Create a new config.

    sz_config = sz_configmanager.create_config_from_template()
    sz_config.add_data_source(data_source_code)

    # Persist the new default config.

    config_definition = sz_config.export()
    config_id = sz_configmanager.set_default_config(config_definition, config_comment)
except SzError as err:
    print(f"\nERROR: {err}\n")
