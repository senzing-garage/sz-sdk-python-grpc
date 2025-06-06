import json

import pytest
from pytest_schema import Regex, schema
from senzing import SzProduct

from senzing_grpc import SzProductGrpc

from .helpers import get_grpc_channel

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_get_license(sz_product: SzProduct) -> None:
    """Test SzProduct.get_license()."""
    actual = sz_product.get_license()
    assert isinstance(actual, str)
    actual_as_dict = json.loads(actual)
    assert schema(get_license_schema) == actual_as_dict


def test_get_version(sz_product: SzProduct) -> None:
    """Test SzProduct.get_version()."""
    actual = sz_product.get_version()
    assert isinstance(actual, str)
    actual_as_dict = json.loads(actual)
    assert schema(get_version_schema) == actual_as_dict


def test_help_1(sz_product: SzProduct) -> None:
    """Test SzProduct.help()."""
    sz_product.help()


def test_help_2(sz_product: SzProduct) -> None:
    """Test SzProduct.help(...)."""
    sz_product.help("get_license")


# -----------------------------------------------------------------------------
# Unique testcases
# -----------------------------------------------------------------------------


def test_constructor() -> None:
    """Test constructor."""
    actual = SzProductGrpc(grpc_channel=get_grpc_channel())
    assert isinstance(actual, SzProduct)


def test_context_management() -> None:
    """Test the use of SzProduct in context."""
    with SzProductGrpc(grpc_channel=get_grpc_channel()) as sz_product:
        actual = sz_product.get_license()
        assert isinstance(actual, str)
        actual_as_dict = json.loads(actual)
        assert schema(get_license_schema) == actual_as_dict


# -----------------------------------------------------------------------------
# Fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_product", scope="function")
def szproduct_fixture() -> SzProduct:
    """
    SzProduct object to use for all tests.
    """
    result = SzProductGrpc(grpc_channel=get_grpc_channel())
    return result


# -----------------------------------------------------------------------------
# Schemas
# -----------------------------------------------------------------------------

get_license_schema = {
    "customer": str,
    "contract": str,
    "issueDate": Regex(r"^\d{4}-\d{2}-\d{2}$"),
    "licenseType": str,
    "licenseLevel": str,
    "billing": str,
    "expireDate": Regex(r"^\d{4}-\d{2}-\d{2}$"),
    "recordLimit": int,
}


get_version_schema = {
    "PRODUCT_NAME": str,
    "VERSION": Regex(r"^([0-9]+)\.([0-9]+)\.([0-9]+)(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?(?:\+[0-9A-Za-z-]+)?$"),
    "BUILD_VERSION": str,
    "BUILD_DATE": Regex(r"^\d{4}-\d{2}-\d{2}$"),
    "BUILD_NUMBER": str,
    "COMPATIBILITY_VERSION": {
        "CONFIG_VERSION": str,
    },
    "SCHEMA_VERSION": {
        "ENGINE_SCHEMA_VERSION": str,
        "MINIMUM_REQUIRED_SCHEMA_VERSION": str,
        "MAXIMUM_REQUIRED_SCHEMA_VERSION": str,
    },
}
