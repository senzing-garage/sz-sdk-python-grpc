#! /usr/bin/env python3

"""
TODO: szabstractfactory.py
"""

# pylint: disable=E1101

from types import TracebackType
from typing import Any, Type, TypedDict, Union

import grpc
from senzing_abstract import (
    SzAbstractFactoryAbstract,
    SzConfigAbstract,
    SzConfigManagerAbstract,
    SzDiagnosticAbstract,
    SzEngineAbstract,
    SzProductAbstract,
)

from .szconfig import SzConfig
from .szconfigmanager import SzConfigManager
from .szdiagnostic import SzDiagnostic
from .szengine import SzEngine
from .szproduct import SzProduct

# Metadata

__all__ = ["SzAbstractFactoryAbstract"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2023-11-27"
__updated__ = "2024-10-24"


# -----------------------------------------------------------------------------
# SzAbstractFactoryParameters class
# -----------------------------------------------------------------------------


class SzAbstractFactoryParameters(TypedDict, total=False):
    """
    SzAbstractFactoryParameters is used to create a dictionary that can be unpacked when creating an SzAbstractFactory.
    """

    grpc_channel: grpc.Channel


# -----------------------------------------------------------------------------
# SzAbstractFactory class
# -----------------------------------------------------------------------------


class SzAbstractFactory(SzAbstractFactoryAbstract):
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

    def create_config(self) -> SzConfigAbstract:
        return SzConfig(grpc_channel=self.channel)

    def create_configmanager(self) -> SzConfigManagerAbstract:
        return SzConfigManager(grpc_channel=self.channel)

    def create_diagnostic(self) -> SzDiagnosticAbstract:
        return SzDiagnostic(grpc_channel=self.channel)

    def create_engine(self) -> SzEngineAbstract:
        return SzEngine(grpc_channel=self.channel)

    def create_product(self) -> SzProductAbstract:
        return SzProduct(grpc_channel=self.channel)

    def reinitialize(self, config_id: int) -> None:
        sz_diagonstic = SzDiagnostic(grpc_channel=self.channel)
        sz_diagonstic._reinitialize(config_id=config_id)  # pylint: disable=W0212

        sz_engine = SzEngine(grpc_channel=self.channel)
        sz_engine._reinitialize(config_id=config_id)  # pylint: disable=W0212
