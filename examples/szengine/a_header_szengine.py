#! /usr/bin/env python3

"""
Simply a header used in development.
"""

from typing import List, Tuple

import grpc
from senzing_truthset import (
    TRUTHSET_CUSTOMER_RECORDS,
    TRUTHSET_REFERENCE_RECORDS,
    TRUTHSET_WATCHLIST_RECORDS,
)

from senzing_grpc import SzEngine, SzEngineFlags

DATA_SOURCES = {
    "CUSTOMERS": TRUTHSET_CUSTOMER_RECORDS,
    "REFERENCE": TRUTHSET_REFERENCE_RECORDS,
    "WATCHLIST": TRUTHSET_WATCHLIST_RECORDS,
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


def add_records(sz_engine: SzEngine, record_id_list: List[Tuple[str, str]]) -> None:
    """Add all of the records in the list."""
    flags = SzEngineFlags.SZ_WITHOUT_INFO
    for record_identification in record_id_list:
        datasource = record_identification[0]
        record_id = record_identification[1]
        record = DATA_SOURCES.get(datasource, {}).get(record_id, {})
        sz_engine.add_record(
            record.get("DataSource", ""),
            record.get("Id", ""),
            record.get("Json", ""),
            flags,
        )


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

print("\n---- szengine --------------------------------------------------------\n")

GRPC_URL = "localhost:8261"
grpc_channel = grpc.insecure_channel(GRPC_URL)
SZ_ENGINE = SzEngine(grpc_channel=grpc_channel)

add_records(SZ_ENGINE, TEST_RECORDS)
