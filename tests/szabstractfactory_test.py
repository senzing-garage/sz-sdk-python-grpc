from datetime import datetime

import grpc
import pytest

from senzing_grpc import (
    SzAbstractFactory,
    SzAbstractFactoryParameters,
    SzConfig,
    SzConfigManager,
    SzDiagnostic,
    SzEngine,
    SzProduct,
)

FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    "grpc_channel": grpc.insecure_channel("localhost:8261"),
}

# -----------------------------------------------------------------------------
# Testcases
# -----------------------------------------------------------------------------


def test_create_sz_config(sz_abstract_factory: SzAbstractFactory) -> None:
    """Create SzConfig."""
    actual = sz_abstract_factory.create_sz_config()
    assert isinstance(actual, SzConfig)


def test_create_sz_configmanager(sz_abstract_factory: SzAbstractFactory) -> None:
    """Create SzConfigManager."""
    actual = sz_abstract_factory.create_sz_configmanager()
    assert isinstance(actual, SzConfigManager)


def test_create_sz_diagnostic(sz_abstract_factory: SzAbstractFactory) -> None:
    """Create SzDiagnostic."""
    actual = sz_abstract_factory.create_sz_diagnostic()
    assert isinstance(actual, SzDiagnostic)


def test_create_sz_engine(sz_abstract_factory: SzAbstractFactory) -> None:
    """Create SzEngine."""
    actual = sz_abstract_factory.create_sz_engine()
    assert isinstance(actual, SzEngine)


def test_create_sz_product(sz_abstract_factory: SzAbstractFactory) -> None:
    """Create SzProduct."""
    actual = sz_abstract_factory.create_sz_product()
    assert isinstance(actual, SzProduct)


def test_reinitialize(sz_abstract_factory: SzAbstractFactory) -> None:
    """Create SzConfig."""

    datasources = [f"TEST_DATASOURCE_{datetime.now().timestamp()}"]

    # Create Senzing objects.

    sz_config = sz_abstract_factory.create_sz_config()
    sz_configmanager = sz_abstract_factory.create_sz_configmanager()

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


def test_destroy(sz_abstract_factory: SzAbstractFactory) -> None:
    """Test a destroy and reinitialize."""
    sz_abstract_factory.destroy()
    sz_engine = sz_abstract_factory.create_sz_engine()
    _ = sz_engine.count_redo_records()


# -----------------------------------------------------------------------------
# Unique testcases
# -----------------------------------------------------------------------------


def test_constructor() -> None:
    """Test constructor."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    actual = SzAbstractFactory(grpc_channel=grpc_channel)
    assert isinstance(actual, SzAbstractFactory)


def test_context() -> None:
    """Test constructor."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    with SzAbstractFactory(grpc_channel=grpc_channel) as actual:
        assert isinstance(actual, SzAbstractFactory)
        sz_config = actual.create_sz_config()
        assert isinstance(sz_config, SzConfig)


# -----------------------------------------------------------------------------
# Fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_abstract_factory", scope="function")
def sz_abstract_factory_fixture() -> SzAbstractFactory:
    """
    Single sz_abstractfactory object to use for all tests.
    """
    result = SzAbstractFactory(**FACTORY_PARAMETERS)
    return result


# -----------------------------------------------------------------------------
# Schemas
# -----------------------------------------------------------------------------
