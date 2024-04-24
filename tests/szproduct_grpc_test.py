import json

import grpc
import pytest
from pytest_schema import Regex, schema

from senzing_grpc import SzEngineFlags, szproduct_grpc

# -----------------------------------------------------------------------------
# SzProduct testcases
# -----------------------------------------------------------------------------


def test_constructor() -> None:
    """Test constructor."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    actual = szproduct_grpc.SzProductGrpc(grpc_channel=grpc_channel)
    assert isinstance(actual, szproduct_grpc.SzProductGrpc)


def test_get_license(sz_product: szproduct_grpc.SzProductGrpc) -> None:
    """Test Senzing license."""
    actual = sz_product.get_license()
    assert isinstance(actual, str)
    actual_json = json.loads(actual)
    assert schema(get_license_schema) == actual_json


def test_get_version(sz_product: szproduct_grpc.SzProductGrpc) -> None:
    """Test Senzing version."""
    actual = sz_product.get_version()
    assert isinstance(actual, str)
    actual_json = json.loads(actual)
    assert schema(get_version_schema) == actual_json


def test_initialize_and_destroy(sz_product: szproduct_grpc.SzProductGrpc) -> None:
    """Test init/destroy cycle."""
    instance_name = "Example"
    settings = {}
    verbose_logging = SzEngineFlags.SZ_NO_LOGGING
    sz_product.initialize(instance_name, settings, verbose_logging)
    sz_product.destroy()


def test_initialize_and_destroy_again(sz_product: szproduct_grpc.SzProductGrpc) -> None:
    """Test init/destroy cycle a second time."""
    instance_name = "Example"
    settings = "{}"
    verbose_logging = SzEngineFlags.SZ_NO_LOGGING
    sz_product.initialize(instance_name, settings, verbose_logging)
    sz_product.destroy()


def test_context_managment() -> None:
    """Test the use of SzProductGrpc in context."""
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    with szproduct_grpc.SzProductGrpc(grpc_channel=grpc_channel) as sz_product:
        actual = sz_product.get_license()
        assert isinstance(actual, str)
        actual_json = json.loads(actual)
        assert schema(get_license_schema) == actual_json


# -----------------------------------------------------------------------------
# SzProduct fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_product", scope="module")  # type: ignore[misc]
def szproduct_fixture() -> szproduct_grpc.SzProductGrpc:
    """
    Single engine object to use for all tests.
    """
    grpc_url = "localhost:8261"
    grpc_channel = grpc.insecure_channel(grpc_url)
    result = szproduct_grpc.SzProductGrpc(grpc_channel=grpc_channel)
    return result


# -----------------------------------------------------------------------------
# SzProduct schemas
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
