from datetime import datetime

import pytest
from senzing import (
    SzAbstractFactory,
    SzConfigManager,
    SzDiagnostic,
    SzEngine,
    SzProduct,
)

from senzing_grpc import SzAbstractFactoryGrpc, SzAbstractFactoryParametersGrpc

from .helpers import get_grpc_channel

FACTORY_PARAMETERS: SzAbstractFactoryParametersGrpc = {
    "grpc_channel": get_grpc_channel(),
}

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_create_configmanager(sz_abstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.create_configmanager()."""
    actual = sz_abstractfactory.create_configmanager()
    assert isinstance(actual, SzConfigManager)


def test_create_diagnostic(sz_abstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.create_diagnostic()."""
    actual = sz_abstractfactory.create_diagnostic()
    assert isinstance(actual, SzDiagnostic)


def test_create_engine(sz_abstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.create_engine()."""
    actual = sz_abstractfactory.create_engine()
    assert isinstance(actual, SzEngine)


def test_create_product(sz_abstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.create_product()."""
    actual = sz_abstractfactory.create_product()
    assert isinstance(actual, SzProduct)


def test_help_1(sz_abstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.help()."""
    sz_abstractfactory.help()


def test_help_2(sz_abstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.help(...)."""
    sz_abstractfactory.help("create_configmanager")

    datasources = [f"TEST_DATASOURCE_{datetime.now().timestamp()}"]

    # Create Senzing objects.

    sz_configmanager = sz_abstractfactory.create_configmanager()
    sz_config = sz_configmanager.create_config_from_template()

    # Add DataSources to Senzing configuration.

    for datasource in datasources:
        sz_config.add_data_source(datasource)

    # Persist new Senzing configuration.

    config_definition = sz_config.export()
    config_id = sz_configmanager.set_default_config(config_definition, "Add My datasources")

    # Update other Senzing objects.

    sz_abstractfactory.reinitialize(config_id)


# -----------------------------------------------------------------------------
# Unique testcases
# -----------------------------------------------------------------------------


def test_constructor() -> None:
    """Test constructor."""
    actual = SzAbstractFactoryGrpc(grpc_channel=get_grpc_channel())
    assert isinstance(actual, SzAbstractFactory)


def test_context() -> None:
    """Test constructor."""
    with SzAbstractFactoryGrpc(grpc_channel=get_grpc_channel()) as actual:
        assert isinstance(actual, SzAbstractFactory)
        sz_config = actual.create_configmanager()
        assert isinstance(sz_config, SzConfigManager)


# -----------------------------------------------------------------------------
# Fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_abstractfactory", scope="function")
def szabstractfactory_fixture() -> SzAbstractFactory:
    """
    SzAbstractFactory object to use for all tests.
    """
    result = SzAbstractFactoryGrpc(**FACTORY_PARAMETERS)
    return result


# -----------------------------------------------------------------------------
# Schemas
# -----------------------------------------------------------------------------
