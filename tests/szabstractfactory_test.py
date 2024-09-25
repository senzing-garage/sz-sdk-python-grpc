import grpc
import pytest
from senzing_abstract import (
    SzAbstractFactoryAbstract,
    SzConfigAbstract,
    SzConfigManagerAbstract,
    SzDiagnosticAbstract,
    SzEngineAbstract,
    SzProductAbstract,
)

from senzing_grpc import SzAbstractFactory

# -----------------------------------------------------------------------------
# SzAbstractFactory testcases
# -----------------------------------------------------------------------------


def test_constructor() -> None:
    """Test constructor."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    actual = SzAbstractFactory(grpc_channel=grpc_channel)
    assert isinstance(actual, SzAbstractFactoryAbstract)


def test_context() -> None:
    """Test constructor."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    with SzAbstractFactory(grpc_channel=grpc_channel) as actual:
        assert isinstance(actual, SzAbstractFactoryAbstract)
        sz_config = actual.create_sz_config()
        assert isinstance(sz_config, SzConfigAbstract)


def test_create_sz_config(szabstractfactory: SzAbstractFactory) -> None:
    """Test SzConfig().add_data_source()."""
    actual = szabstractfactory.create_sz_config()
    assert isinstance(actual, SzConfigAbstract)


def test_create_sz_configmanager(szabstractfactory: SzAbstractFactory) -> None:
    """Test SzConfig().add_data_source()."""
    actual = szabstractfactory.create_sz_configmanager()
    assert isinstance(actual, SzConfigManagerAbstract)


def test_create_sz_diagnostic(szabstractfactory: SzAbstractFactory) -> None:
    """Test SzConfig().add_data_source()."""
    actual = szabstractfactory.create_sz_diagnostic()
    assert isinstance(actual, SzDiagnosticAbstract)


def test_create_sz_engine(szabstractfactory: SzAbstractFactory) -> None:
    """Test SzConfig().add_data_source()."""
    actual = szabstractfactory.create_sz_engine()
    assert isinstance(actual, SzEngineAbstract)


def test_create_sz_product(szabstractfactory: SzAbstractFactory) -> None:
    """Test SzConfig().add_data_source()."""
    actual = szabstractfactory.create_sz_product()
    assert isinstance(actual, SzProductAbstract)


# -----------------------------------------------------------------------------
# SzAbstractFactory fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="szabstractfactory", scope="module")
def szabstractfactory_fixture() -> SzAbstractFactory:
    """
    Single sz_abstractfactory object to use for all tests.
    """
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    result = SzAbstractFactory(grpc_channel=grpc_channel)
    return result
