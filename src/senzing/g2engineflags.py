#! /usr/bin/env python3

"""
TODO: g2engineflags.py
"""

# TODO: Fix the duplication of this file with g2-sdk-python-next.

from enum import IntFlag
from typing import Any, List

# Metadata

__all__ = ["G2EngineFlags"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2023-10-30"
__updated__ = "2023-10-30"

# -----------------------------------------------------------------------------
# G2EngineFlags class
# -----------------------------------------------------------------------------


class G2EngineFlags(IntFlag):
    """Engine Flags ..."""

    @classmethod
    def combine_flags(
        cls, list_of_strings: List[str], *args: Any, **kwargs: Any
    ) -> int:
        """OR together all strings in list_of_strings"""
        # pylint: disable=unused-argument

        result = 0
        for string in list_of_strings:
            result = result | G2EngineFlags[string]
        return result

    # Flags for exporting entity data.

    G2_EXPORT_INCLUDE_RESOLVED = 1 << 0
    G2_EXPORT_INCLUDE_POSSIBLY_SAME = 1 << 1
    G2_EXPORT_INCLUDE_POSSIBLY_RELATED = 1 << 2
    G2_EXPORT_INCLUDE_NAME_ONLY = 1 << 3
    G2_EXPORT_INCLUDE_DISCLOSED = 1 << 4
    G2_EXPORT_INCLUDE_SINGLETONS = 1 << 5
    G2_EXPORT_INCLUDE_ALL_ENTITIES = (
        G2_EXPORT_INCLUDE_RESOLVED | G2_EXPORT_INCLUDE_SINGLETONS
    )
    G2_EXPORT_INCLUDE_ALL_RELATIONSHIPS = (
        G2_EXPORT_INCLUDE_POSSIBLY_SAME
        | G2_EXPORT_INCLUDE_POSSIBLY_RELATED
        | G2_EXPORT_INCLUDE_NAME_ONLY
        | G2_EXPORT_INCLUDE_DISCLOSED
    )

    # Flags for outputting entity relation data.

    G2_ENTITY_INCLUDE_POSSIBLY_SAME_RELATIONS = 1 << 6
    G2_ENTITY_INCLUDE_POSSIBLY_RELATED_RELATIONS = 1 << 7
    G2_ENTITY_INCLUDE_NAME_ONLY_RELATIONS = 1 << 8
    G2_ENTITY_INCLUDE_DISCLOSED_RELATIONS = 1 << 9
    G2_ENTITY_INCLUDE_ALL_RELATIONS = (
        G2_ENTITY_INCLUDE_POSSIBLY_SAME_RELATIONS
        | G2_ENTITY_INCLUDE_POSSIBLY_RELATED_RELATIONS
        | G2_ENTITY_INCLUDE_NAME_ONLY_RELATIONS
        | G2_ENTITY_INCLUDE_DISCLOSED_RELATIONS
    )

    # Flags for outputting entity feature data.

    G2_ENTITY_INCLUDE_ALL_FEATURES = 1 << 10
    G2_ENTITY_INCLUDE_REPRESENTATIVE_FEATURES = 1 << 11

    # Flags for getting extra information about an entity.

    G2_ENTITY_INCLUDE_ENTITY_NAME = 1 << 12
    G2_ENTITY_INCLUDE_RECORD_SUMMARY = 1 << 13
    G2_ENTITY_INCLUDE_RECORD_DATA = 1 << 14
    G2_ENTITY_INCLUDE_RECORD_MATCHING_INFO = 1 << 15
    G2_ENTITY_INCLUDE_RECORD_JSON_DATA = 1 << 16
    G2_ENTITY_INCLUDE_RECORD_FORMATTED_DATA = 1 << 17
    G2_ENTITY_INCLUDE_RECORD_FEATURE_IDS = 1 << 18
    G2_ENTITY_INCLUDE_RELATED_ENTITY_NAME = 1 << 19
    G2_ENTITY_INCLUDE_RELATED_MATCHING_INFO = 1 << 20
    G2_ENTITY_INCLUDE_RELATED_RECORD_SUMMARY = 1 << 21
    G2_ENTITY_INCLUDE_RELATED_RECORD_DATA = 1 << 22

    # Flags for extra feature data.

    G2_ENTITY_OPTION_INCLUDE_INTERNAL_FEATURES = 1 << 23
    G2_ENTITY_OPTION_INCLUDE_FEATURE_STATS = 1 << 24

    # Flags for finding entity path data.

    G2_FIND_PATH_PREFER_EXCLUDE = 1 << 25

    # Flags for including search result information.

    G2_INCLUDE_FEATURE_SCORES = 1 << 26
    G2_SEARCH_INCLUDE_STATS = 1 << 27
    G2_SEARCH_INCLUDE_FEATURE_SCORES = G2_INCLUDE_FEATURE_SCORES

    # Flags for exporting entity data.

    G2_SEARCH_INCLUDE_RESOLVED = G2_EXPORT_INCLUDE_RESOLVED
    G2_SEARCH_INCLUDE_POSSIBLY_SAME = G2_EXPORT_INCLUDE_POSSIBLY_SAME
    G2_SEARCH_INCLUDE_POSSIBLY_RELATED = G2_EXPORT_INCLUDE_POSSIBLY_RELATED
    G2_SEARCH_INCLUDE_NAME_ONLY = G2_EXPORT_INCLUDE_NAME_ONLY
    G2_SEARCH_INCLUDE_ALL_ENTITIES = (
        G2_SEARCH_INCLUDE_RESOLVED
        | G2_SEARCH_INCLUDE_POSSIBLY_SAME
        | G2_SEARCH_INCLUDE_POSSIBLY_RELATED
        | G2_SEARCH_INCLUDE_NAME_ONLY
    )

    # Recommended settings.

    G2_RECORD_DEFAULT_FLAGS = G2_ENTITY_INCLUDE_RECORD_JSON_DATA
    G2_ENTITY_DEFAULT_FLAGS = (
        G2_ENTITY_INCLUDE_ALL_RELATIONS
        | G2_ENTITY_INCLUDE_REPRESENTATIVE_FEATURES
        | G2_ENTITY_INCLUDE_ENTITY_NAME
        | G2_ENTITY_INCLUDE_RECORD_SUMMARY
        | G2_ENTITY_INCLUDE_RECORD_DATA
        | G2_ENTITY_INCLUDE_RECORD_MATCHING_INFO
        | G2_ENTITY_INCLUDE_RELATED_ENTITY_NAME
        | G2_ENTITY_INCLUDE_RELATED_RECORD_SUMMARY
        | G2_ENTITY_INCLUDE_RELATED_MATCHING_INFO
    )
    G2_ENTITY_BRIEF_DEFAULT_FLAGS = (
        G2_ENTITY_INCLUDE_RECORD_MATCHING_INFO
        | G2_ENTITY_INCLUDE_ALL_RELATIONS
        | G2_ENTITY_INCLUDE_RELATED_MATCHING_INFO
    )
    G2_EXPORT_DEFAULT_FLAGS = (
        G2_EXPORT_INCLUDE_ALL_ENTITIES
        | G2_EXPORT_INCLUDE_ALL_RELATIONSHIPS
        | G2_ENTITY_INCLUDE_ALL_RELATIONS
        | G2_ENTITY_INCLUDE_REPRESENTATIVE_FEATURES
        | G2_ENTITY_INCLUDE_ENTITY_NAME
        | G2_ENTITY_INCLUDE_RECORD_DATA
        | G2_ENTITY_INCLUDE_RECORD_MATCHING_INFO
        | G2_ENTITY_INCLUDE_RELATED_MATCHING_INFO
    )
    G2_FIND_PATH_DEFAULT_FLAGS = (
        G2_ENTITY_INCLUDE_ALL_RELATIONS
        | G2_ENTITY_INCLUDE_ENTITY_NAME
        | G2_ENTITY_INCLUDE_RECORD_SUMMARY
        | G2_ENTITY_INCLUDE_RELATED_MATCHING_INFO
    )
    G2_WHY_ENTITY_DEFAULT_FLAGS = (
        G2_ENTITY_DEFAULT_FLAGS
        | G2_ENTITY_INCLUDE_RECORD_FEATURE_IDS
        | G2_ENTITY_OPTION_INCLUDE_INTERNAL_FEATURES
        | G2_ENTITY_OPTION_INCLUDE_FEATURE_STATS
        | G2_INCLUDE_FEATURE_SCORES
    )
    G2_HOW_ENTITY_DEFAULT_FLAGS = (
        G2_ENTITY_DEFAULT_FLAGS
        | G2_ENTITY_INCLUDE_RECORD_FEATURE_IDS
        | G2_ENTITY_OPTION_INCLUDE_INTERNAL_FEATURES
        | G2_ENTITY_OPTION_INCLUDE_FEATURE_STATS
        | G2_INCLUDE_FEATURE_SCORES
    )

    G2_SEARCH_BY_ATTRIBUTES_ALL = (
        G2_SEARCH_INCLUDE_ALL_ENTITIES
        | G2_ENTITY_INCLUDE_REPRESENTATIVE_FEATURES
        | G2_ENTITY_INCLUDE_ENTITY_NAME
        | G2_ENTITY_INCLUDE_RECORD_SUMMARY
        | G2_SEARCH_INCLUDE_FEATURE_SCORES
    )
    G2_SEARCH_BY_ATTRIBUTES_STRONG = (
        G2_SEARCH_INCLUDE_RESOLVED
        | G2_SEARCH_INCLUDE_POSSIBLY_SAME
        | G2_ENTITY_INCLUDE_REPRESENTATIVE_FEATURES
        | G2_ENTITY_INCLUDE_ENTITY_NAME
        | G2_ENTITY_INCLUDE_RECORD_SUMMARY
        | G2_SEARCH_INCLUDE_FEATURE_SCORES
    )
    G2_SEARCH_BY_ATTRIBUTES_MINIMAL_ALL = G2_SEARCH_INCLUDE_ALL_ENTITIES
    G2_SEARCH_BY_ATTRIBUTES_MINIMAL_STRONG = (
        G2_SEARCH_INCLUDE_RESOLVED | G2_SEARCH_INCLUDE_POSSIBLY_SAME
    )
    G2_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS = G2_SEARCH_BY_ATTRIBUTES_ALL
