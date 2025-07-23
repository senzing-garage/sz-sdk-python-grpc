"""
TODO: szhelpers.py
"""

import json
from collections.abc import Callable
from contextlib import suppress
from functools import wraps
from typing import Any, Dict, TypeVar, Union
from typing import cast as typing_cast

import grpc
from senzing import ENGINE_EXCEPTION_MAP, SzError, SzSdkError

# Metadata

__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2025-01-10"
__updated__ = "2025-01-16"


_F = TypeVar("_F", bound=Callable[..., Any])

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

        if details:

            # Find JSON string.

            start_of_json = details.find("{")

            if start_of_json > 0:
                details = details[start_of_json:]

            # Parse JSON.

            details_dict = {}
            try:
                details_dict = json.loads(details)
            except Exception:  # pylint: disable=W0718
                return result

            errors_reason = extract_reason(details_dict)

            # errors_reason = details_dict.get("reason", "")
            senzing_error_code = get_senzing_error_code(errors_reason)
            senzing_error_class = ENGINE_EXCEPTION_MAP.get(senzing_error_code, SzError)
            result = senzing_error_class(details)

    return result


def extract_reason(candidate_dict: Dict[Any, Any]) -> str:
    if "reason" in candidate_dict:
        return str(candidate_dict.get("reason"))
    if "error" in candidate_dict:
        next_dict = candidate_dict.get("error")
        if isinstance(next_dict, dict):
            return extract_reason(next_dict)
    return ""


def catch_sdk_exceptions(func_to_decorate: _F) -> _F:
    """
    The Python SDK methods convert Python types to ctypes and utilize helper functions. If incorrect types/values are
    used standard library exceptions are raised not SzError exceptions as the Senzing library hasn't been called
    yet. Raise the original Python exception type and append information to identify the SDK method called, accepted
    arguments & types and the arguments and types the SDK method received. Also convert ctypes.ArgumentError exceptions
    to TypeError, a user shouldn't need to import ctypes to catch ArgumentError

    :meta private:
    """

    @wraps(func_to_decorate)
    def wrapped_func(*args: Any, **kwargs: Any) -> _F:
        try:
            return typing_cast(_F, func_to_decorate(*args, **kwargs))
        except (TypeError, ValueError) as err:
            # Get wrapped function annotation, remove unwanted keys
            annotations_dict = func_to_decorate.__annotations__
            with suppress(KeyError):
                del annotations_dict["return"]
                del annotations_dict["kwargs"]

            # Get the wrapped function signature names and types and build a string to append to the error message
            func_signature = ", ".join(
                [
                    f"{name}: {type if isinstance(type, str) else type.__name__}"
                    for name, type in annotations_dict.items()
                ]
            )

            method_and_signature = f"{func_to_decorate.__module__}.{func_to_decorate.__name__}({func_signature})"
            append_err_msg = f" - expected: {method_and_signature}"

            arg_0 = err.args[0]
            if " missing " in err.args[0] and " required positional argument" in err.args[0]:
                arg_0 = " ".join(err.args[0].split()[1:])
            new_arg_0 = f"calling {method_and_signature}" if not err.args else f"{arg_0}{append_err_msg}"
            err.args = (new_arg_0,) + err.args[1:]

            raise SzSdkError(err) from err

    return typing_cast(_F, wrapped_func)
