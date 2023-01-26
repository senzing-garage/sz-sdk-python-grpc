import json


class G2DiagnosticClient:
    def __init__(self):
        self.type = None
        self.connector = None

    #internal methods
    def legacy_init_grpc_connector(self, url, module_name, ini_params):
        import g2_diagnostic_grpc_connector
        self.type = 'GRPC'
        self.connector = g2_diagnostic_grpc_connector.G2DiagnosticGRPCConnector()
        return self.connector.init(url, module_name, ini_params)

    def __init_grpc_connector(self):
        import g2_diagnostic_grpc_connector
        self.type = 'GRPC'
        self.connector = g2_diagnostic_grpc_connector.G2DiagnosticGRPCConnector()

    def __init_direct_connector(self):
        import g2_diagnostic_direct_connector
        self.type = 'DIRECT'
        self.connector = g2_diagnostic_direct_connector.G2DiagnosticDirectConnector()

    #startup/shutdown methods
    def init_grpc_connection_with_url(self, url):
        self.__init_grpc_connector()
        self.connector.init_with_url(url)

    def init_direct(self, module_name, ini_params, verbose_logging=False):
        self.__init_direct_connector()
        if isinstance(ini_params, dict):
            ini_params = json.dumps(ini_params)

        return self.connector.init(
            module_name=module_name,
            iniParams=ini_params,
            verboseLogging=verbose_logging
            )

    def init_direct_from_environment(self, module_name, verbose_logging=False):
        self.__init_direct_connector()
        return self.connector.init_direct_from_environment(
            module_name=module_name,
            verbose_logging=verbose_logging
            )

    def init_with_config_id(self, config_id):
        self.__init_direct_connector()
        config_id = int(config_id)
        return self.connector.init_direct_with_config_id(config_id=config_id)

    def reinit(self, config_id):
        config_id = int(config_id)
        return self.connector.reinit(config_id=config_id)

    def destroy(self):
        retval = self.connector.destroy()
        self.type = None
        self.connector = None
        return retval

    #get sys into methods
    def get_physical_cores(self):
        return self.connector.get_physical_cores()

    def get_logical_cores(self):
        return self.connector.get_logical_cores()

    def get_available_memory(self):
        return self.connector.get_available_memory()

    def get_total_system_memory(self):
        return self.connector.get_total_system_memory()

    def check_db_perf(self, seconds_to_run):
        return self.connector.check_db_perf(seconds_to_run=seconds_to_run)

    def get_db_info(self, return_as_string=False):
        return self.connector.get_db_info(return_as_string=return_as_string)

    #data query methods
    def get_entity_details(self,
                           entity_id,
                           include_internal_features=False,
                           return_as_string=False):
        entity_id = int(entity_id)
        include_internal_features = int(include_internal_features)
        return self.connector.get_entity_details(
            entity_id=entity_id,
            include_internal_features=include_internal_features,
            return_as_string=return_as_string
            )

    def get_relationship_details(self,
                                 relationship_id,
                                 include_internal_features=False,
                                 return_as_string=False):
        relationship_id = int(relationship_id)
        include_internal_features = int(include_internal_features)
        return self.connector.get_relationship_details(
            relationship_id=relationship_id,
            include_internal_features=include_internal_features,
            return_as_string=return_as_string
            )

    def get_entity_resume(self, entity_id, return_as_string=False):
        entity_id = int(entity_id)
        return self.connector.get_entity_resume(
            entity_id=entity_id,
            return_as_string=return_as_string
            )

    def get_feature(self, lib_feat_id, return_as_string=False):
        lib_feat_id = int(lib_feat_id)
        return self.connector.get_feature(
            lib_feat_id=lib_feat_id,
            return_as_string=return_as_string
            )

    def find_entities_by_feature_ids(self, features, return_as_string=False):
        if isinstance(features, int):
            features = str(features)
        if isinstance(features, (list, tuple)) is False:
            features = [features]
        features = json.dumps(features)
        return self.connector.find_entities_by_feature_ids(
            features=features,
            return_as_string=return_as_string
            )

    def get_entity_list_by_size_request(self, entity_size):
        entity_size = int(entity_size)
        return self.connector.get_entity_list_by_size_request(entity_size=entity_size)

    def fetch_next_entity_by_size(self, handle):
        return self.connector.fetch_next_entity_by_size(handle)

    def close_entity_list_by_size(self, handle):
        return self.connector.close_entity_list_by_size(handle)

    def get_entity_list_by_size_return_list(self, entity_size):
        return self.connector.get_entity_list_by_size_return_list(entity_size)

    def get_entity_list_by_size_with_callback(self, entity_size, callback):
        return self.connector.get_entity_list_by_size_with_callback(
            entity_size=entity_size,
            callback=callback
            )

    #stats methods
    def get_enity_size_breakdown(self,
                                 minimum_entity_size,
                                 include_internal_features=False,
                                 return_as_string=False):
        return self.connector.get_entity_size_breakdown(
            minimum_entity_size=minimum_entity_size,
            include_internal_features=include_internal_features,
            return_as_string=return_as_string
            )

    def get_data_source_counts(self, return_as_string=False):
        return self.connector.get_data_source_counts(return_as_string=return_as_string)

    def get_mapping_statistics(self, include_internal_features=False, return_as_string=False):
        return self.connector.get_mapping_statistics(
            include_internal_features=include_internal_features,
            return_as_string=return_as_string
            )

    def get_resolution_statistics(self, return_as_string=False):
        return self.connector.get_resolution_statistics(return_as_string=return_as_string)

    def get_generic_features(self, feature_type, maximum_estimated_count, return_as_string=False):
        return self.connector.get_generic_features(
            feature_type=feature_type,
            maximum_estimated_count=maximum_estimated_count,
            return_as_string=return_as_string
            )
