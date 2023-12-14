import json

import grpc
import pytest
from pytest_schema import Regex, schema

from senzing_grpc import g2product_grpc

# -----------------------------------------------------------------------------
# G2Product fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="g2_product", scope="module")  # type: ignore[misc]
def g2product_fixture() -> g2product_grpc.G2ProductGrpc:
    """
    Single engine object to use for all tests.
    """
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    result = g2product_grpc.G2ProductGrpc(grpc_channel=grpc_channel)
    return result


# -----------------------------------------------------------------------------
# G2Product schemas
# -----------------------------------------------------------------------------

license_schema = {
    "customer": str,
    "contract": str,
    "issueDate": Regex(r"^\d{4}-\d{2}-\d{2}$"),
    "licenseType": str,
    "licenseLevel": str,
    "billing": str,
    "expireDate": Regex(r"^\d{4}-\d{2}-\d{2}$"),
    "recordLimit": int,
}


version_schema = {
    "PRODUCT_NAME": str,
    "VERSION": Regex(
        r"^([0-9]+)\.([0-9]+)\.([0-9]+)(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?(?:\+[0-9A-Za-z-]+)?$"
    ),
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


# -----------------------------------------------------------------------------
# G2Product testcases
# -----------------------------------------------------------------------------


def test_constructor() -> None:
    """Test constructor."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    actual = g2product_grpc.G2ProductGrpc(grpc_channel=grpc_channel)
    assert isinstance(actual, g2product_grpc.G2ProductGrpc)


def test_license(g2_product: g2product_grpc.G2ProductGrpc) -> None:
    """Test Senzing license."""
    actual = g2_product.license()
    assert isinstance(actual, str)
    actual_json = json.loads(actual)
    assert schema(license_schema) == actual_json


def test_version(g2_product: g2product_grpc.G2ProductGrpc) -> None:
    """Test Senzing version."""
    actual = g2_product.version()
    assert isinstance(actual, str)
    actual_json = json.loads(actual)
    assert schema(version_schema) == actual_json


def test_init_and_destroy(g2_product: g2product_grpc.G2ProductGrpc) -> None:
    """Test init/destroy cycle."""
    g2_product.init("Example", "{}", 0)
    g2_product.destroy()


def test_init_and_destroy_again(g2_product: g2product_grpc.G2ProductGrpc) -> None:
    """Test init/destroy cycle a second time."""
    g2_product.init("Example", "{}", 0)
    g2_product.destroy()


def test_context_managment() -> None:
    """Test the use of G2ProductGrpc in context."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    with g2product_grpc.G2ProductGrpc(grpc_channel=grpc_channel) as g2_product:
        actual = g2_product.license()
        assert isinstance(actual, str)
        actual_json = json.loads(actual)
        assert schema(license_schema) == actual_json
