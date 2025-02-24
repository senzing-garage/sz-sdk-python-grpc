from datetime import datetime

import pytest
from senzing import (
    SzAbstractFactory,
    SzConfig,
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


def test_create_config(sz_abstract_factory: SzAbstractFactory) -> None:
    """Create SzConfig."""
    actual = sz_abstract_factory.create_config()
    assert isinstance(actual, SzConfig)


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

    sz_config = sz_abstract_factory.create_config()
    sz_configmanager = sz_abstract_factory.create_configmanager()

    # Get existing Senzing configuration.

    old_config_id = sz_configmanager.get_default_config_id()
    old_json_config = sz_configmanager.get_config(old_config_id)
    config_handle = sz_config.import_config(old_json_config)

    # Add DataSources to existing Senzing configuration.

    for datasource in datasources:
        sz_config.add_data_source(config_handle, datasource)

    # Persist new Senzing configuration.

    new_json_config = sz_config.export_config(config_handle)
    new_config_id = sz_configmanager.add_config(new_json_config, "Add My datasources")
    sz_configmanager.replace_default_config_id(old_config_id, new_config_id)

    # Update other Senzing objects.

    sz_abstract_factory.reinitialize(new_config_id)


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
        sz_config = actual.create_config()
        assert isinstance(sz_config, SzConfig)


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
