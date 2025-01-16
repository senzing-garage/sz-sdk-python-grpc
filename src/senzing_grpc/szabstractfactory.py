#! /usr/bin/env python3

"""
TODO: szabstractfactory.py
"""

# pylint: disable=E1101

from types import TracebackType
from typing import Any, Type, TypedDict, Union

import grpc
from senzing import (
    SzAbstractFactory,
    SzConfig,
    SzConfigManager,
    SzDiagnostic,
    SzEngine,
    SzProduct,
)

from .szconfig import SzConfigGrpc
from .szconfigmanager import SzConfigManagerGrpc
from .szdiagnostic import SzDiagnosticGrpc
from .szengine import SzEngineGrpc
from .szproduct import SzProductGrpc

# Metadata

__all__ = ["SzAbstractFactoryGrpc", "SzAbstractFactoryParametersGrpc"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2025-01-10"
__updated__ = "2025-01-16"


# -----------------------------------------------------------------------------
# SzAbstractFactoryParametersGrpc class
# -----------------------------------------------------------------------------


class SzAbstractFactoryParametersGrpc(TypedDict, total=False):
    """
    SzAbstractFactoryParameters is used to create a dictionary that can be unpacked when creating an SzAbstractFactory.
    """

    grpc_channel: grpc.Channel


# -----------------------------------------------------------------------------
# SzAbstractFactoryGrpc class
# -----------------------------------------------------------------------------


class SzAbstractFactoryGrpc(SzAbstractFactory):
    """
    SzAbstractFactory module is a factory pattern for accessing Senzing over gRPC.
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
    # SzAbstractFactory methods
    # -------------------------------------------------------------------------

    def create_config(self) -> SzConfig:
        return SzConfigGrpc(grpc_channel=self.channel)

    def create_configmanager(self) -> SzConfigManager:
        return SzConfigManagerGrpc(grpc_channel=self.channel)

    def create_diagnostic(self) -> SzDiagnostic:
        return SzDiagnosticGrpc(grpc_channel=self.channel)

    def create_engine(self) -> SzEngine:
        return SzEngineGrpc(grpc_channel=self.channel)

    def create_product(self) -> SzProduct:
        return SzProductGrpc(grpc_channel=self.channel)

    def reinitialize(self, config_id: int) -> None:
        sz_diagonstic = SzDiagnosticGrpc(grpc_channel=self.channel)
        sz_diagonstic._reinitialize(config_id=config_id)  # pylint: disable=W0212

        sz_engine = SzEngineGrpc(grpc_channel=self.channel)
        sz_engine._reinitialize(config_id=config_id)  # pylint: disable=W0212
