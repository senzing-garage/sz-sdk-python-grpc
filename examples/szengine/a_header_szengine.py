#! /usr/bin/env python3

"""
Simply a header used in development.
"""

from typing import List, Tuple

import grpc
from senzing import SZ_WITHOUT_INFO, SzEngine
from senzing_truthset import (
    TRUTHSET_CUSTOMER_RECORDS,
    TRUTHSET_REFERENCE_RECORDS,
    TRUTHSET_WATCHLIST_RECORDS,
)

from senzing_grpc import SzAbstractFactoryGrpc, SzAbstractFactoryParametersGrpc

DATA_SOURCES = {
    "CUSTOMERS": TRUTHSET_CUSTOMER_RECORDS,
    "REFERENCE": TRUTHSET_REFERENCE_RECORDS,
    "WATCHLIST": TRUTHSET_WATCHLIST_RECORDS,
}
FACTORY_PARAMETERS: SzAbstractFactoryParametersGrpc = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}

TEST_RECORDS: List[Tuple[str, str]] = [
    ("CUSTOMERS", "1001"),
    ("CUSTOMERS", "1002"),
    ("CUSTOMERS", "1003"),
    ("CUSTOMERS", "1009"),
]

# -----------------------------------------------------------------------------
# Internal functions
# -----------------------------------------------------------------------------


def add_records(sz_engine_local: SzEngine, record_id_list: List[Tuple[str, str]]) -> None:
    """Add all of the records in the list."""
    flags = SZ_WITHOUT_INFO
    for record_identification in record_id_list:
        datasource = record_identification[0]
        record_id = record_identification[1]
        record = DATA_SOURCES.get(datasource, {}).get(record_id, {})
        sz_engine_local.add_record(
            record.get("DataSource", ""),
            record.get("Id", ""),
            record.get("Json", ""),
            flags,
        )


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

print("\n---- szengine --------------------------------------------------------\n")

sz_abstract_factory = SzAbstractFactoryGrpc(**FACTORY_PARAMETERS)
sz_engine = sz_abstract_factory.create_engine()
add_records(sz_engine, TEST_RECORDS)
