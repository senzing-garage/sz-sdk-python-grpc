#! /usr/bin/env python3

import json

import grpc

from senzing_grpc import (
    SzAbstractFactory,
    SzAbstractFactoryParameters,
    SzEngineFlags,
    SzError,
)

ATTRIBUTES = json.dumps({"NAME_FULL": "BOB SMITH", "EMAIL_ADDRESS": "bsmith@work.com"})
FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}
FLAGS = SzEngineFlags.SZ_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS
SEARCH_PROFILE = ""

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_engine = sz_abstract_factory.create_engine()
    RESULT = sz_engine.search_by_attributes(ATTRIBUTES, FLAGS, SEARCH_PROFILE)
    print(f"\nFile {__file__}:\n{RESULT}\n")
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
