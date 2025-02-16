#! /usr/bin/env python3

"""
``senzing_grpc.szconfigmanager.SzConfigManagerGrpc`` is a `gRPC`_ implementation
of the `senzing.szconfigmanager.SzConfigManager`_ interface.

.. _gRPC: https://grpc.io
.. _senzing.szconfigmanager.SzConfigManager: https://garage.senzing.com/sz-sdk-python/senzing.html#module-senzing.szconfigmanager
"""

# pylint: disable=E1101

from types import TracebackType
from typing import Any, Dict, Type, Union

import grpc
from senzing import SzConfigManager

from .pb2_grpc import szconfigmanager_pb2, szconfigmanager_pb2_grpc
from .szhelpers import as_str, new_exception

# Metadata

__all__ = ["SzConfigManagerGrpc"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2025-01-10"
__updated__ = "2025-01-16"

SENZING_PRODUCT_ID = (
    "5051"  # See https://github.com/senzing-garage/knowledge-base/blob/main/lists/senzing-component-ids.md
)

# -----------------------------------------------------------------------------
# SzConfigManagerGrpc class
# -----------------------------------------------------------------------------


class SzConfigManagerGrpc(SzConfigManager):
    """
    SzConfigManager module access library over gRPC.
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
        self.stub = szconfigmanager_pb2_grpc.SzConfigManagerStub(self.channel)

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
    # SzConfigManager methods
    # -------------------------------------------------------------------------

    def add_config(
        self,
        config_definition: str,
        config_comment: str,
    ) -> int:
        try:
            request = szconfigmanager_pb2.AddConfigRequest(  # type: ignore[unused-ignore]
                config_definition=as_str(config_definition),
                config_comment=as_str(config_comment),
            )
            response = self.stub.AddConfig(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def _destroy(self) -> None:
        """Null function in the sz-sdk-python-grpc implementation."""

    def get_config(self, config_id: int) -> str:
        try:
            request = szconfigmanager_pb2.GetConfigRequest(config_id=config_id)  # type: ignore[unused-ignore]
            response = self.stub.GetConfig(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_configs(self) -> str:
        try:
            request = szconfigmanager_pb2.GetConfigsRequest()  # type: ignore[unused-ignore]
            response = self.stub.GetConfigs(request)
            return str(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def get_default_config_id(self) -> int:
        try:
            request = szconfigmanager_pb2.GetDefaultConfigIdRequest()  # type: ignore[unused-ignore]
            response = self.stub.GetDefaultConfigId(request)
            return int(response.result)
        except Exception as err:
            raise new_exception(err) from err

    def _initialize(
        self,
        instance_name: str,
        settings: Union[str, Dict[Any, Any]],
        verbose_logging: int = 0,
    ) -> None:
        """Null function in the sz-sdk-python-grpc implementation."""
        _ = instance_name
        _ = settings
        _ = verbose_logging

    def replace_default_config_id(self, current_default_config_id: int, new_default_config_id: int) -> None:
        try:
            request = szconfigmanager_pb2.ReplaceDefaultConfigIdRequest(  # type: ignore[unused-ignore]
                current_default_config_id=current_default_config_id,
                new_default_config_id=new_default_config_id,
            )
            self.stub.ReplaceDefaultConfigId(request)
        except Exception as err:
            raise new_exception(err) from err

    def set_default_config_id(self, config_id: int) -> None:
        try:
            request = szconfigmanager_pb2.SetDefaultConfigIdRequest(  # type: ignore[unused-ignore]
                config_id=config_id,
            )
            self.stub.SetDefaultConfigId(request)
        except Exception as err:
            raise new_exception(err) from err
