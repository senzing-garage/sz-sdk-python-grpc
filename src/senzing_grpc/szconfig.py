#! /usr/bin/env python3

"""
``senzing_grpc.szconfig.SzConfigGrpc`` is a `gRPC`_ implementation
of the `senzing.szconfig.SzConfig`_ interface.

.. _gRPC: https://grpc.io
.. _senzing.szconfig.SzConfig: https://garage.senzing.com/sz-sdk-python/senzing.html#module-senzing.szconfig
"""

# pylint: disable=E1101

from types import TracebackType
from typing import Any, Dict, Type, Union

import grpc
from senzing import SzConfig
from senzing_grpc_protobuf import szconfig_pb2, szconfig_pb2_grpc

from .szhelpers import new_exception

# Metadata

__all__ = ["SzConfigGrpc"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2025-01-10"
__updated__ = "2025-01-16"

SENZING_PRODUCT_ID = (
    "5050"  # See https://github.com/senzing-garage/knowledge-base/blob/main/lists/senzing-component-ids.md
)

# -----------------------------------------------------------------------------
# SzConfigGrpc class
# -----------------------------------------------------------------------------


class SzConfigGrpc(SzConfig):
    """
    SzConfig module access library over gRPC.
    """

    # -------------------------------------------------------------------------
    # Python dunder/magic methods
    # -------------------------------------------------------------------------

    def __init__(
        self,
        grpc_channel: grpc.Channel,
    ) -> None:
        """
        Constructor

        For return value of -> None, see https://peps.python.org/pep-0484/#the-meaning-of-annotations
        """

        self.channel = grpc_channel
        self.stub = szconfig_pb2_grpc.SzConfigStub(self.channel)
        self.config_definition = ""

    def __enter__(
        self,
    ) -> Any:  # TODO: Replace "Any" with "Self" once python 3.11 is lowest supported python version.
        """Context Manager method."""
        return self

    def __exit__(
        self,
        exc_type: Union[Type[BaseException], None],
        exc_val: Union[BaseException, None],
        exc_tb: Union[TracebackType, None],
    ) -> None:
        """Context Manager method."""

    # -------------------------------------------------------------------------
    # SzConfig interface methods
    # -------------------------------------------------------------------------

    def register_data_source(
        self,
        data_source_code: str,
    ) -> str:
        try:
            request = szconfig_pb2.RegisterDataSourceRequest(  # type: ignore[unused-ignore]
                config_definition=self.config_definition, data_source_code=data_source_code
            )
            response = self.stub.RegisterDataSource(request)
            config_definition = response.config_definition
            if len(config_definition) > 0:
                self.config_definition = config_definition
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def unregister_data_source(self, data_source_code: str) -> str:
        try:
            request = szconfig_pb2.UnregisterDataSourceRequest(config_definition=self.config_definition, data_source_code=data_source_code)  # type: ignore[unused-ignore]
            response = self.stub.UnregisterDataSource(request)
            config_definition = response.config_definition
            if len(config_definition) > 0:
                self.config_definition = config_definition
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def export(self) -> str:
        return self.config_definition

    def get_data_source_registry(self) -> str:
        try:
            request = szconfig_pb2.GetDataSourceRegistryRequest(config_definition=self.config_definition)  # type: ignore[unused-ignore]
            response = self.stub.GetDataSourceRegistry(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    # -------------------------------------------------------------------------
    # Non-public SzConfigCore methods
    # -------------------------------------------------------------------------

    def _destroy(self) -> None:
        """Null function in the sz-sdk-python-grpc implementation."""

    def import_config_definition(self, config_definition: str) -> None:
        """
        Set the internal JSON document.

        Args:
            config_definition (str): A Senzing configuration JSON document.
        """
        self.config_definition = config_definition

    def import_template(
        self,
    ) -> None:
        """
        Retrieves a Senzing configuration from the default template.
        The default template is the Senzing configuration JSON document file,
        g2config.json, located in the PIPELINE.RESOURCEPATH path.
        """

    def initialize(
        self,
        instance_name: str,
        settings: Union[str, Dict[Any, Any]],
        verbose_logging: int = 0,
    ) -> None:
        """Null function in the sz-sdk-python-grpc implementation."""
        _ = instance_name
        _ = settings
        _ = verbose_logging

    def verify_config_definition(self, config_definition: str) -> bool:
        """
        Determine if configuration definition is valid.

        Args:
            config_definition (str): A Senzing configuration JSON document.
        """
        request = szconfig_pb2.VerifyConfigRequest(config_definition=config_definition)  # type: ignore[unused-ignore]
        response = self.stub.VerifyConfig(request)
        return bool(response.result)
