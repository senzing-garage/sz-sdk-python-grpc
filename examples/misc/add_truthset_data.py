#! /usr/bin/env python3

import grpc
from senzing_truthset import (
    TRUTHSET_CUSTOMER_RECORDS,
    TRUTHSET_REFERENCE_RECORDS,
    TRUTHSET_WATCHLIST_RECORDS,
)

from senzing_grpc import (
    SZ_WITHOUT_INFO,
    SzAbstractFactory,
    SzAbstractFactoryParameters,
    SzError,
)

FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_engine = sz_abstract_factory.create_engine()
    record_sets = [
        TRUTHSET_CUSTOMER_RECORDS,
        TRUTHSET_REFERENCE_RECORDS,
        TRUTHSET_WATCHLIST_RECORDS,
    ]
    for record_set in record_sets:
        for record in record_set.values():
            sz_engine.add_record(
                record.get("DataSource"),
                record.get("Id"),
                record.get("Json"),
                SZ_WITHOUT_INFO,
            )
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
