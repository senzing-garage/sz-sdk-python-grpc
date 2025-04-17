"""
TODO: szhelpers.py
"""

import json
from typing import Any, Dict, Union

import grpc
from senzing import ENGINE_EXCEPTION_MAP, SzError

# Metadata

__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2025-01-10"
__updated__ = "2025-01-16"

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


def get_senzing_error_code(error_text: str) -> int:
    """
    Given an exception string, find the exception code.

    :meta private:
    """
    if len(error_text) == 0:
        return 0
    exception_message_splits = error_text.split("|", 1)
    try:
        result = int(exception_message_splits[0].strip().lstrip("SENZ"))
    except ValueError:
        print(f"ERROR: Could not parse error text '{error_text}'")
        result = 9999
    return result


def new_exception(initial_exception: Exception) -> Exception:
    """
    Given an exception, determine which Senzing exception is is.

    Args:
        initial_exception (Exception): An unknown Exception

    Returns:
        Exception: Either a SzError or the original exception.
    """

    result = initial_exception

    if isinstance(initial_exception, grpc.RpcError):

        details = initial_exception.details()  # type: ignore[unused-ignore]

        # Find JSON string.

        start_of_json = details.find("{")

        if start_of_json > 0:
            details = details[start_of_json:]

        # Parse JSON.

        details_dict = {}
        try:
            details_dict = json.loads(details)
        except Exception:  # pylint: disable=W0718
            details_dict = {}
        errors_reason = details_dict.get("reason", "")
        senzing_error_code = get_senzing_error_code(errors_reason)
        senzing_error_class = ENGINE_EXCEPTION_MAP.get(senzing_error_code, SzError)
        result = senzing_error_class(details)

    return result
