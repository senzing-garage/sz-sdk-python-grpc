#! /usr/bin/env python3

import grpc

from senzing_grpc import (
    SzAbstractFactory,
    SzAbstractFactoryParameters,
    SzEngineFlags,
    SzError,
)

DATA_SOURCE_CODE_1 = "CUSTOMERS"
DATA_SOURCE_CODE_2 = "CUSTOMERS"
FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}
FLAGS = SzEngineFlags.SZ_WHY_ENTITIES_DEFAULT_FLAGS
RECORD_ID_1 = "1001"
RECORD_ID_2 = "1002"

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_engine = sz_abstract_factory.create_sz_engine()
    RESULT = sz_engine.why_records(
        DATA_SOURCE_CODE_1,
        RECORD_ID_1,
        DATA_SOURCE_CODE_2,
        RECORD_ID_2,
        FLAGS,
    )
    print(f"\nFile {__file__}:\n{RESULT}\n")
except SzError as err:
    print(f"\nError in {__file__}:\n{err}\n")
