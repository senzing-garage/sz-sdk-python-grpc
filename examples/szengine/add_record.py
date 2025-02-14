#! /usr/bin/env python3

import json

import grpc
from senzing import SzEngineFlags, SzError

from senzing_grpc import SzAbstractFactoryGrpc

DATA_SOURCE_CODE = "TEST"
FLAGS = SzEngineFlags.SZ_WITH_INFO
RECORD_DEFINITION = json.dumps(
    {
        "RECORD_TYPE": "PERSON",
        "PRIMARY_NAME_LAST": "Smith",
        "PRIMARY_NAME_FIRST": "Robert",
        "DATE_OF_BIRTH": "12/11/1978",
        "ADDR_TYPE": "MAILING",
        "ADDR_LINE1": "123 Main Street, Las Vegas NV 89132",
        "PHONE_TYPE": "HOME",
        "PHONE_NUMBER": "702-919-1300",
        "EMAIL_ADDRESS": "bsmith@work.com",
        "DATE": "1/2/18",
        "STATUS": "Active",
        "AMOUNT": "100",
    }
)
RECORD_ID = "1"
try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_engine = sz_abstract_factory.create_engine()
    RESULT = sz_engine.add_record(DATA_SOURCE_CODE, RECORD_ID, RECORD_DEFINITION, FLAGS)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
