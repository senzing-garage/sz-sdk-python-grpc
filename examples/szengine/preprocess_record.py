#! /usr/bin/env python3

import grpc
from senzing import SzEngineFlags, SzError

from senzing_grpc import SzAbstractFactoryGrpc, SzAbstractFactoryParametersGrpc

FACTORY_PARAMETERS: SzAbstractFactoryParametersGrpc = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}
FLAGS = SzEngineFlags.SZ_RECORD_DEFAULT_FLAGS
RECORD_DEFINITION = (
    "{"
    '"RECORD_TYPE": "PERSON",'
    '"PRIMARY_NAME_LAST": "Smith",'
    '"PRIMARY_NAME_FIRST": "Robert",'
    '"DATE_OF_BIRTH": "12/11/1978",'
    '"ADDR_TYPE": "MAILING",'
    '"ADDR_LINE1": "123 Main Street, Las Vegas NV 89132",'
    '"PHONE_TYPE": "HOME",'
    '"PHONE_NUMBER": "702-919-1300",'
    '"EMAIL_ADDRESS": "bsmith@work.com",'
    '"DATE": "1/2/18",'
    '"STATUS": "Active",'
    '"AMOUNT": "100"'
    "}"
)

try:
    sz_abstract_factory = SzAbstractFactoryGrpc(**FACTORY_PARAMETERS)
    sz_engine = sz_abstract_factory.create_engine()
    RESULT = sz_engine.preprocess_record(RECORD_DEFINITION, FLAGS)
    print(f"\nFile {__file__}:\n{RESULT}\n")
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
