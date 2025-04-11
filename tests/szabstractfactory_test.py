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
# Testcases
# -----------------------------------------------------------------------------


def test_create_configmanager(sz_abstract_factory: SzAbstractFactory) -> None:
    """Create SzConfigManager."""
    actual = sz_abstract_factory.create_configmanager()
    assert isinstance(actual, SzConfigManager)


def test_create_diagnostic(sz_abstract_factory: SzAbstractFactory) -> None:
    """Create SzDiagnostic."""
    actual = sz_abstract_factory.create_diagnostic()
    assert isinstance(actual, SzDiagnostic)


def test_create_engine(sz_abstract_factory: SzAbstractFactory) -> None:
    """Create SzEngine."""
    actual = sz_abstract_factory.create_engine()
    assert isinstance(actual, SzEngine)


def test_create_product(sz_abstract_factory: SzAbstractFactory) -> None:
    """Create SzProduct."""
    actual = sz_abstract_factory.create_product()
    assert isinstance(actual, SzProduct)


def test_reinitialize(sz_abstract_factory: SzAbstractFactory) -> None:
    """Create SzConfig."""

    datasources = [f"TEST_DATASOURCE_{datetime.now().timestamp()}"]

    # Create Senzing objects.

    sz_configmanager = sz_abstract_factory.create_configmanager()
    sz_config = sz_configmanager.create_config_from_template()

    # Add DataSources to Senzing configuration.

    for datasource in datasources:
        sz_config.add_data_source(datasource)

    # Persist new Senzing configuration.

    config_definition = sz_config.export()
    config_id = sz_configmanager.set_default_config(config_definition, "Add My datasources")

    # Update other Senzing objects.

    sz_abstract_factory.reinitialize(config_id)


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


@pytest.fixture(name="sz_abstract_factory", scope="function")
def sz_abstract_factory_fixture() -> SzAbstractFactory:
    """
    Single SzAbstractFactoryGrpc object to use for all tests.
    """
    result = SzAbstractFactoryGrpc(**FACTORY_PARAMETERS)
    return result


# -----------------------------------------------------------------------------
# Schemas
# -----------------------------------------------------------------------------
