#! /usr/bin/env python3

import grpc

from senzing_grpc import SzConfigManager, SzError

GRPC_URL = "localhost:8261"

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_configmanager = SzConfigManager(grpc_channel=grpc_channel)
    CONFIG_LIST = sz_configmanager.get_config_list()
    print(CONFIG_LIST[:66], "...")
except SzError as err:
    print(f"\nError:\n{err}\n")
