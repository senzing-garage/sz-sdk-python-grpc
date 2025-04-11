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

from .pb2_grpc import szconfig_pb2, szconfig_pb2_grpc
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

    def add_data_source(
        self,
        data_source_code: str,
    ) -> str:
        try:
            request = szconfig_pb2.AddDataSourceRequest(  # type: ignore[unused-ignore]
                config_definition=self.config_definition, data_source_code=data_source_code
            )
            response = self.stub.AddDataSource(request)
            config_definition = response.config_definition
            if len(config_definition) > 0:
                self.config_definition = config_definition
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def delete_data_source(self, data_source_code: str) -> str:
        try:
            request = szconfig_pb2.DeleteDataSourceRequest(config_definition=self.config_definition, data_source_code=data_source_code)  # type: ignore[unused-ignore]
            response = self.stub.DeleteDataSource(request)
            config_definition = response.config_definition
            if len(config_definition) > 0:
                self.config_definition = config_definition
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def export(self) -> str:
        return self.config_definition

    def get_data_sources(self) -> str:
        try:
            request = szconfig_pb2.GetDataSourcesRequest(config_definition=self.config_definition)  # type: ignore[unused-ignore]
            response = self.stub.GetDataSources(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    # -------------------------------------------------------------------------
    # Non-public SzConfigCore methods
    # -------------------------------------------------------------------------

    def _destroy(self) -> None:
        """Null function in the sz-sdk-python-grpc implementation."""

    def import_config_definition(self, config_definition: str) -> int:
        """
        Set the internal JSON document.

        Args:
            config_definition (str): A Senzing configuration JSON document.
        """
        self.config_definition = config_definition

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
