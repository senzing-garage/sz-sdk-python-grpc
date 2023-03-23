import sys
import json
import warnings

try:
    from senzing import G2Diagnostic
except ModuleNotFoundError:
    warnings.warn('Cannot import Senzing python libraries.')
    warnings.warn('Please verify your PYTHONPATH includes the path to senzing python libs')
    warnings.warn('Environment can be setup by sourcing "setupEnv" '\
                  'from your senzing project directory')
    sys.exit(-1)


class G2DiagnosticDirectConnector:
    def __init__(self):
        self.g2_handle = None

    # startup/shutdown methods
    def init_direct(self, module_name, ini_params, config_id, verbose_logging):
        if isinstance(ini_params, str):
            ini_params = json.loads(ini_params)
        self.g2_handle = G2Diagnostic()
        if not config_id:
            return self.g2_handle.init(module_name, ini_params, verbose_logging)
        else:
            return self.g2_handle.initWithConfigID(module_name, ini_params, config_id, verbose_logging)

    def init_with_url(self, url):
        warnings.warn('init_with_url is not valid for direct connections')

    def init_direct_from_environment(self, module_name, config_id, verbose_logging):
        import senzing_module_config
        json_config = senzing_module_config.get_json_config()
        self.g2_handle = G2Diagnostic()
        if not config_id:
            return self.g2_handle.init(module_name, json_config, verbose_logging)
        else:
            return self.g2_handle.initWithConfigID(module_name, json_config, config_id, verbose_logging)

    def reinit(self, config_id):
        config_id = bytes(config_id, 'utf-8')
        self.g2_handle.reinit(config_id)

    def destroy(self):
        self.g2_handle.destroy()
        self.g2_handle = None

    # get sys into methods
    def get_physical_cores(self):
        return self.g2_handle.getPhysicalCores()

    def get_logical_cores(self):
        return self.g2_handle.getLogicalCores()

    def get_available_memory(self):
        return self.g2_handle.getAvailableMemory()

    def get_total_system_memory(self):
        return self.g2_handle.getTotalSystemMemory()

    def check_db_perf(self, seconds_to_run, return_as_string=False):
        seconds_to_run = int(seconds_to_run)
        response = bytearray()
        self.g2_handle.checkDBPerf(seconds_to_run, response=response)
        response = response.decode()
        if not return_as_string:
            response = json.loads(response)
        return response

    def get_db_info(self, return_as_string=False):
        response = bytearray()
        self.g2_handle.getDBInfo(response=response)
        response = response.decode()
        if not return_as_string:
            response = json.loads(response)
        return response

    # data query methods
    def get_entity_details(self,
                           entity_id,
                           include_internal_features=False,
                           return_as_string=False):
        entity_id = int(entity_id)
        include_internal_features = int(include_internal_features)

        response = bytearray()
        self.g2_handle.getEntityDetails(
            entityID=entity_id,
            includeInternalFeatures=include_internal_features,
            response=response
            )

        #convert from bytebuffer to string
        response = response.decode()

        #maybe convert to dict
        if not return_as_string:
            response = json.loads(response)
        return response

    def get_relationship_details(self,
                                 relationship_id,
                                 include_internal_features=False,
                                 return_as_string=False):
        relationship_id = int(relationship_id)
        include_internal_features = int(include_internal_features)

        response = bytearray()
        self.g2_handle.getRelationshipDetails(
            relationshipID=relationship_id,
            includeInternalFeatures=include_internal_features,
            response=response
            )

        #convert from bytebuffer to string
        response = response.decode()

        #maybe convert to dict
        if not return_as_string:
            response = json.loads(response)
        return response

    def get_entity_resume(self, entity_id, return_as_string=False):
        entity_id = int(entity_id)
        response = bytearray()
        self.g2_handle.getEntityResume(entityID=entity_id, response=response)

        #convert from bytebuffer to string
        response = response.decode()

        #maybe convert to dict
        if not return_as_string:
            response = json.loads(response)
        return response

    def get_feature(self, lib_feat_id, return_as_string=False):
        lib_feat_id = int(lib_feat_id)
        response = bytearray()
        self.g2_handle.getFeature(libFeatID=lib_feat_id, response=response)

        #convert from bytebuffer to string
        response = response.decode()

        #maybe convert to dict
        if not return_as_string:
            response = json.loads(response)
        return response

    def find_entities_by_feature_ids(self, features, return_as_string=False):
        response = bytearray()
        self.g2_handle.findEntitiesByFeatureIDs(features=features, response=response)

        #convert from bytebuffer to string
        response = response.decode()

        #maybe convert to dict
        if not return_as_string:
            response = json.loads(response)
        return response

    def get_entity_list_by_size_request(self, entity_size):
        entity_size = int(entity_size)
        response = bytearray()
        handle = self.g2_handle.getEntityListBySize(entitySize=entity_size, response=response)
        return handle

    def fetch_next_entity_by_size(self, handle):
        fetch_data = bytearray()
        self.g2_handle.fetchNextEntityBySize(sizedEntityHandle=handle, response=fetch_data)
        if not fetch_data:
            return None
        return fetch_data.decode().strip()

    def close_entity_list_by_size(self, handle):
        return self.g2_handle.closeEntityListBySize(sizedEntityHandle=handle)

    def get_entity_list_by_size_return_list(self, entity_size):
        result_set = []
        handle = self.get_entity_list_by_size_request(entity_size=entity_size)

        while True:
            queried_entity = self.fetch_next_entity_by_size(handle=handle)
            if not queried_entity:
                break
            queried_entity = json.loads(queried_entity)
            result_set.extend(queried_entity)

        self.close_entity_list_by_size(handle=handle)
        return result_set

    def get_entity_list_by_size_with_callback(self, entity_size, callback, return_as_string=False):
        handle = self.get_entity_list_by_size_request(entity_size=entity_size)

        while True:
            queried_entity = self.fetch_next_entity_by_size(handle=handle)
            if not queried_entity:
                break
            if return_as_string:
                callback(queried_entity)
            else:
                callback(json.loads(queried_entity))

        self.close_entity_list_by_size(handle=handle)

    def get_entity_list_by_size_iteritems(self, entity_size, return_as_string=False):
        handle = self.get_entity_list_by_size_request(entity_size=entity_size)

        while True:
            queried_entity = self.fetch_next_entity_by_size(handle=handle)
            if not queried_entity:
                break
            if return_as_string:
                yield queried_entity
            else:
                yield json.loads(queried_entity)

        self.close_entity_list_by_size(handle=handle)


    # stats methods
    def get_entity_size_breakdown(self,
                                  minimum_entity_size,
                                  include_internal_features=False,
                                  return_as_string=False):
        response = bytearray()
        self.g2_handle.getEntitySizeBreakdown(
            minimumEntitySize=minimum_entity_size,
            includeInternalFeatures=include_internal_features,
            response=response
            )
        response = response.decode()
        if not return_as_string:
            response = json.loads(response)
        return response

    def get_data_source_counts(self, return_as_string=False):
        response = bytearray()
        self.g2_handle.getDataSourceCounts(response=response)
        response = response.decode()
        if not return_as_string:
            response = json.loads(response)
        return response

    def get_mapping_statistics(self, include_internal_features=False, return_as_string=False):
        response = bytearray()
        self.g2_handle.getMappingStatistics(
            includeInternalFeatures=include_internal_features,
            response=response
            )
        response = response.decode()
        if not return_as_string:
            response = json.loads(response)
        return response

    def get_resolution_statistics(self, return_as_string=False):
        response = bytearray()
        self.g2_handle.getResolutionStatistics(response=response)
        response = response.decode()
        if not return_as_string:
            response = json.loads(response)
        return response

    def get_generic_features(self, feature_type, maximum_estimated_count, return_as_string=False):
        response = bytearray()
        self.g2_handle.getGenericFeatures(
            featureType=feature_type,
            maximumEstimatedCount=maximum_estimated_count,
            response=response
            )
        response = response.decode()
        if not return_as_string:
            response = json.loads(response)
        return response
