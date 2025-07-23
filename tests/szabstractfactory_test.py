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


def test_destroy(sz_abstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.create_product()."""
    sz_abstractfactory.destroy()


def test_help_1(sz_abstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.help()."""
    sz_abstractfactory.help()


def test_help_2(sz_abstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.help(...)."""
    sz_abstractfactory.help("create_configmanager")


def test_reinitialize(sz_abstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.reinitialize()."""

    datasource = f"Test_Datasource_{datetime.now().timestamp()}"
    config_comment = f"Test_config_{datetime.now().timestamp()}"

    # Create Senzing objects.

    sz_diagnostic = sz_abstractfactory.create_diagnostic()
    sz_engine = sz_abstractfactory.create_engine()
    sz_configmanager = sz_abstractfactory.create_configmanager()

    # Use Senzing objects.

    _ = sz_diagnostic.get_repository_info()
    _ = sz_engine.add_record("TEST", "787B", '{"NAME_FULL":"Testy McTester"}')
    old_active_config_id = sz_engine.get_active_config_id()

    # Add DataSources to Senzing configuration.

    old_default_config_id = sz_configmanager.get_default_config_id()

    assert old_active_config_id == old_default_config_id

    sz_config = sz_configmanager.create_config_from_config_id(old_default_config_id)
    sz_config.register_data_source(datasource)

    # Persist new Senzing configuration.

    config_definition = sz_config.export()
    new_default_config_id = sz_configmanager.set_default_config(config_definition, config_comment)

    assert old_active_config_id != new_default_config_id

    # Update Senzing objects.

    sz_abstractfactory.reinitialize(new_default_config_id)

    # Use Senzing objects.

    _ = sz_diagnostic.get_repository_info()
    new_active_config_id = sz_engine.get_active_config_id()

    assert new_active_config_id == new_default_config_id


# -----------------------------------------------------------------------------
# candidates
# -----------------------------------------------------------------------------


# def test_create_same_settings(sz_abstractfactory: SzAbstractFactory) -> None:
#     """Test SzAbstractFactoryGrpc with the same settings."""
#     sz_abstractfactory_2 = SzAbstractFactoryGrpc(**FACTORY_PARAMETERS)
#     assert sz_abstractfactory is sz_abstractfactory_2


# def test_create_with_different_settings(sz_abstractfactory: SzAbstractFactory) -> None:
#     """Test SzAbstractFactoryCore with different settings."""
#     _ = sz_abstractfactory
#     factory_parameters: SzAbstractFactoryParametersGrpc = {
#         "grpc_channel": grpc.insecure_channel("localhost:8261"),
#     }
#     with pytest.raises(SzSdkError):
#         SzAbstractFactoryGrpc(**factory_parameters)


# -----------------------------------------------------------------------------
# Unique testcases
# -----------------------------------------------------------------------------


def test_close_factory() -> None:
    sz_abstract_factory = SzAbstractFactoryGrpc(grpc_channel=get_grpc_channel())
    _ = sz_abstract_factory.create_engine()
    sz_abstract_factory.destroy()
    _ = sz_abstract_factory.create_engine()


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
