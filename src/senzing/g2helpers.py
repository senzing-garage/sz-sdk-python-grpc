"""
TODO: g2helpers.py
"""

import json
from typing import Any, Dict, Union

import grpc  # type: ignore

from . import g2exception

# -----------------------------------------------------------------------------
# Helpers for working with parameters
# -----------------------------------------------------------------------------


def as_str(candidate_value: Union[str, Dict[Any, Any]]) -> str:
    """
    Given a string or dict, return a str.

    Args:
        candidate_value (Union[str, Dict[Any, Any]]): _description_

    Returns:
        str: The string representation of the candidate_value
    """
    if isinstance(candidate_value, dict):
        return json.dumps(candidate_value)
    return candidate_value


# -----------------------------------------------------------------------------
# Helpers for working with errors
# -----------------------------------------------------------------------------


def new_exception(initial_exception: Exception) -> Exception:
    """
    Given an exception, determine which Senzing exception is is.

    Args:
        initial_exception (Exception): An unknown Exception

    Returns:
        Exception: Either a G2Exception or the original exception.
    """

    result = initial_exception

    if isinstance(initial_exception, grpc.RpcError):
        details = initial_exception.details()  # type: ignore[unused-ignore]
        details_dict = {}
        try:
            details_dict = json.loads(details)
        except Exception:  # pylint: disable=W0718
            pass
        errors_list = details_dict.get("errors", [])
        senzing_error_code = 0
        for an_error in errors_list:
            senzing_error_code = g2exception.get_senzing_error_code(an_error)
            if senzing_error_code > 0:
                break

        senzing_error_class = g2exception.EXCEPTION_MAP.get(
            senzing_error_code, g2exception.G2Exception
        )
        result = senzing_error_class(details)

    return result
