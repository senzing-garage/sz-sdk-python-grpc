#! /usr/bin/env python3

import grpc
from senzing import (
    SzAbstractFactory,
    SzConfig,
    SzConfigManager,
    SzDiagnostic,
    SzEngine,
    SzError,
    SzProduct,
)

from senzing_grpc import SzAbstractFactoryGrpc


def try_sz_abstract_factory(sz_abstract_factory_local: SzAbstractFactory) -> None:
    """Just a test of parameter typing."""
    _ = sz_abstract_factory_local


def try_sz_config(sz_config_local: SzConfig) -> None:
    """Just a test of parameter typing."""
    _ = sz_config_local


def try_sz_configmanager(sz_configmanager_local: SzConfigManager) -> None:
    """Just a test of parameter typing."""
    _ = sz_configmanager_local


def try_sz_diagnostic(sz_diagnostic_local: SzDiagnostic) -> None:
    """Just a test of parameter typing."""
    _ = sz_diagnostic_local


def try_sz_engine(sz_engine_local: SzEngine) -> None:
    """Just a test of parameter typing."""
    _ = sz_engine_local


def try_sz_product(sz_product_local: SzProduct) -> None:
    """Just a test of parameter typing."""
    _ = sz_product_local


try:
    grpc_channel = grpc.insecure_channel("localhost:8261")
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel)
    sz_config = sz_abstract_factory.create_config()
    sz_configmanager = sz_abstract_factory.create_configmanager()
    sz_diagnostic = sz_abstract_factory.create_diagnostic()
    sz_engine = sz_abstract_factory.create_engine()
    sz_product = sz_abstract_factory.create_product()

    try_sz_abstract_factory(sz_abstract_factory)
    try_sz_config(sz_config)
    try_sz_configmanager(sz_configmanager)
    try_sz_diagnostic(sz_diagnostic)
    try_sz_engine(sz_engine)
    try_sz_product(sz_product)

except SzError as err:
    print(f"\nERROR: {err}\n")
