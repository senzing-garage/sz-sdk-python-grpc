import sys
import warnings

try:
    from senzing import G2EngineFlags
except ModuleNotFoundError:
    warnings.warn('Cannot import Senzing python libraries.')
    warnings.warn('Please verify your PYTHONPATH includes the path to senzing python libs')
    warnings.warn('Environment can be setup by sourcing "setupEnv" '\
                  'from your senzing project directory')
    sys.exit(-1)

class G2Flags:
    def __init__(self):
        self.flags = 0

    def clear_flags(self):
        self.flags = 0

    def get_flags(self):
        return self.flags

    # Flags for outputting entity relation data.
    def set_entity_include_possibly_same_relations(self):
        self.flags |= G2EngineFlags.G2_ENTITY_INCLUDE_POSSIBLY_SAME_RELATIONS

    def set_entity_include_possibly_related_relations(self):
        self.flags |= G2EngineFlags.G2_ENTITY_INCLUDE_POSSIBLY_RELATED_RELATIONS

    def set_entity_include_name_only_relations(self):
        self.flags |= G2EngineFlags.G2_ENTITY_INCLUDE_NAME_ONLY_RELATIONS

    def set_entity_include_disclosed_relations(self):
        self.flags |= G2EngineFlags.G2_ENTITY_INCLUDE_DISCLOSED_RELATIONS

    def set_entity_include_all_relations(self):
        self.flags |= G2EngineFlags.G2_ENTITY_INCLUDE_ALL_RELATIONS

    # Flags for outputting entity feature data.
    def set_entity_include_all_features(self):
        self.flags |= G2EngineFlags.G2_ENTITY_INCLUDE_ALL_FEATURES

    def set_entity_include_representative_features(self):
        self.flags |= G2EngineFlags.G2_ENTITY_INCLUDE_REPRESENTATIVE_FEATURES

    # Flags for getting extra information about an entity.
    def set_entity_include_entity_name(self):
        self.flags |= G2EngineFlags.G2_ENTITY_INCLUDE_ENTITY_NAME
    
    def set_entity_include_record_summary(self):
        self.flags |= G2EngineFlags.G2_ENTITY_INCLUDE_RECORD_SUMMARY

    def set_entitY_include_record_data(self):
        self.flags |= G2EngineFlags.G2_ENTITY_INCLUDE_RECORD_DATA 

    def set_entity_include_record_matching_info(self):
        self.flags |= G2EngineFlags.G2_ENTITY_INCLUDE_RECORD_MATCHING_INFO

    def set_entity_include_record_json_data(self):
        self.flags |= G2EngineFlags.G2_ENTITY_INCLUDE_RECORD_JSON_DATA

    def set_entity_include_record_formatted_data(self):
        self.flags |= G2EngineFlags.G2_ENTITY_INCLUDE_RECORD_FORMATTED_DATA

    def set_entity_include_record_feature_ids(self):
        self.flags |= G2EngineFlags.G2_ENTITY_INCLUDE_RECORD_FEATURE_IDS

    def set_entity_include_related_entity_name(self):
        self.flags |= G2EngineFlags.G2_ENTITY_INCLUDE_RELATED_ENTITY_NAME

    def set_entity_include_related_matching_info(self):
        self.flags |= G2EngineFlags.G2_ENTITY_INCLUDE_RELATED_MATCHING_INFO

    def set_entity_include_related_record_summary(self):
        self.flags |= G2EngineFlags.G2_ENTITY_INCLUDE_RELATED_RECORD_SUMMARY 

    def set_entity_inlcude_related_record_data(self):
        self.flags |= G2EngineFlags.G2_ENTITY_INCLUDE_RELATED_RECORD_DATA 

    # Flags for bulk exporting entity data
    def set_export_include_resolved(self):
        self.flags |= G2EngineFlags.G2_EXPORT_INCLUDE_RESOLVED

    def set_export_include_possibly_same(self):
        self.flags |= G2EngineFlags.G2_EXPORT_INCLUDE_POSSIBLY_SAME

    def set_export_include_possibly_related(self):
        self.flags |= G2EngineFlags.G2_EXPORT_INCLUDE_POSSIBLY_RELATED

    def set_export_include_name_only(self):
        self.flags |= G2EngineFlags.G2_EXPORT_INCLUDE_NAME_ONLY

    def set_export_include_disclosed(self):
        self.flags |= G2EngineFlags.G2_EXPORT_INCLUDE_DISCLOSED

    def set_export_include_singletons(self):
        self.flags |= G2EngineFlags.G2_EXPORT_INCLUDE_SINGLETONS

    def set_export_include_all_entities(self):
        self.flags |= G2EngineFlags.G2_EXPORT_INCLUDE_ALL_ENTITIES
    
    def set_export_include_all_relationships(self):
        self.flags |= G2EngineFlags.G2_EXPORT_INCLUDE_ALL_RELATIONSHIPS    

    # Flags for extra feature data.
    def set_entity_option_include_internal_features(self):
        self.flags |= G2EngineFlags.G2_ENTITY_OPTION_INCLUDE_INTERNAL_FEATURES

    def set_entity_option_include_feature_stats(self):
        self.flags |= G2EngineFlags.G2_ENTITY_OPTION_INCLUDE_FEATURE_STATS

    # Flags for finding entity path data.
    def set_find_path_prefer_exclude(self):
        self.flags |= G2EngineFlags.G2_FIND_PATH_PREFER_EXCLUDE

    # Flags for including search result information.
    def set_search_include_feature_scores(self):
        self.flags |= G2EngineFlags.G2_INCLUDE_FEATURE_SCORES 

    def set_search_include_stats(self):
        self.flags |= G2EngineFlags.G2_SEARCH_INCLUDE_STATS

    def set_search_include_feature_scores(self):
        self.flags |= G2EngineFlags.G2_SEARCH_INCLUDE_FEATURE_SCORES

    # Flags for searching entity data.
    def set_search_include_resolved(self):
        self.flags |= G2EngineFlags.G2_SEARCH_INCLUDE_RESOLVED

    def set_search_include_possibly_same(self):
        self.flags |= G2EngineFlags.G2_SEARCH_INCLUDE_POSSIBLY_SAME
    
    def set_search_include_possibly_related(self):
        self.flags |= G2EngineFlags.G2_SEARCH_INCLUDE_POSSIBLY_RELATED
    
    def set_search_include_name_only(self):
        self.flags |= G2EngineFlags.G2_SEARCH_INCLUDE_NAME_ONLY
    
    def set_search_include_all_entities(self):
        self.flags |= G2EngineFlags.G2_SEARCH_INCLUDE_ALL_ENTITIES

    # Recommended settings
    def set_record_default_flags(self):
        self.flags |= G2EngineFlags.G2_RECORD_DEFAULT_FLAGS
    
    def set_entity_default_flags(self):
        self.flags |= G2EngineFlags.G2_ENTITY_DEFAULT_FLAGS

    def set_entity_brief_default_flags(self):
        self.flags |= G2EngineFlags.G2_ENTITY_BRIEF_DEFAULT_FLAGS

    def set_export_default_flags(self):
        self.flags |= G2EngineFlags.G2_EXPORT_DEFAULT_FLAGS
    
    def set_find_path_default_flags(self):
        self.flags |= G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS
    
    def set_why_entity_default_flags(self):
        self.flags |= G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS

    def set_how_entity_default_flags(self):
        self.flags |= G2EngineFlags.G2_HOW_ENTITY_DEFAULT_FLAGS

    def set_search_by_attribtues_all(self):
        self.flags |= G2EngineFlags.G2_SEARCH_BY_ATTRIBUTES_ALL

    def set_search_by_attributes_strong(self):
        self.flags |= G2EngineFlags.G2_SEARCH_BY_ATTRIBUTES_STRONG

    def set_search_by_attributes_minimal_all(self):
        self.flags |= G2EngineFlags.G2_SEARCH_BY_ATTRIBUTES_MINIMAL_ALL
    
    def set_search_by_attribtues_minimal_strong(self):
        self.flags |= G2EngineFlags.G2_SEARCH_BY_ATTRIBUTES_MINIMAL_STRONG
    
    def set_search_by_attributes_default_flags(self):
        self.flags |= G2EngineFlags.G2_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS


class G2RecordFlags(G2Flags):
    def __init__(self):
        super().__init__()
        self.set_record_default_flags()

class G2EntityFlags(G2Flags):
    def __init__(self):
        super().__init__()
        self.set_entity_default_flags()

class G2ExportFlags(G2Flags):
    def __init__(self):
        super().__init__()
        self.set_export_default_flags()

class G2FindPathFlags(G2Flags):
    def __init__(self):
        super().__init__()
        self.set_find_path_default_flags()

class G2WhyEntityFlags(G2Flags):
    def __init__(self):
        super().__init__()
        self.set_why_entity_default_flags()

class G2HowEntityFlags(G2Flags):
    def __init__(self):
        super().__init__()
        self.set_how_entity_default_flags()

class G2SearchByAttribtuesFlags(G2Flags):
    def __init__(self):
        self.set_search_by_attributes_default_flags()

    def set_search_by_attribtues_all(self):
        self.clear_flags()
        super().set_search_by_attributes_all()

    def set_search_by_attributes_strong(self):
        self.clear_flags()
        super().set_search_by_attributes_strong()

    def set_search_by_attributes_minimal_all(self):
        self.clear_flags()
        super().set_search_by_attributes_minimal_all()
    
    def set_search_by_attribtues_minimal_strong(self):
        self.clear_flags()
        super().set_search_by_attributes_minimal_strong()
    
    def set_search_by_attributes_default_flags(self):
        self.clear_flags()
        super().set_search_by_attributes_default_flags()



