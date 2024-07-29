#! /usr/bin/env python3

import grpc
from senzing_truthset import (
    TRUTHSET_CUSTOMER_RECORDS,
    TRUTHSET_REFERENCE_RECORDS,
    TRUTHSET_WATCHLIST_RECORDS,
)

from senzing_grpc import SZ_WITHOUT_INFO, SzEngine, SzError

GRPC_URL = "localhost:8261"

try:
    grpc_channel = grpc.insecure_channel(GRPC_URL)
    sz_engine = SzEngine(grpc_channel=grpc_channel)
    record_sets = [
        TRUTHSET_CUSTOMER_RECORDS,
        TRUTHSET_REFERENCE_RECORDS,
        TRUTHSET_WATCHLIST_RECORDS,
    ]
    FLAGS = SZ_WITHOUT_INFO
    for record_set in record_sets:
        for record in record_set.values():
            sz_engine.add_record(
                record.get("DataSource"), record.get("Id"), record.get("Json"), FLAGS
            )
except SzError as err:
    print(f"\nError:\n{err}\n")
