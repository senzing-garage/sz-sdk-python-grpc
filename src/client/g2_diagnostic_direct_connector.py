import grpc
import sys
import json
import warnings

try:
    from senzing import G2Exception, G2Diagnostic
except ModuleNotFoundError:
    print('Cannot import Senzing python libraries.  please verify your PYTHONPATH includes the path to senzing python libs')
    print('Environment can be setup by sourcing "setupEnv" from your senzing project directory')
    sys.exit(-1)


class G2DiagnosticDirectConnector:
    def __init__(self):
        self.g2_handle = None
        self.json_config = None


    # startup/shutdown methods

    #GGANOTE: depricate when server configs itself
    def init(self, url, moduleName, iniParams, verboseLogging=False):
        if isinstance(iniParams,dict):
            iniParams = json.dumps(iniParams)
        return_code = self.g2_handle.init(moduleName, self.json_config, verboseLogging)


    def init_with_url(self, url):
        warnings.warn('init_with_url is not valid for direct connections')

    def init_direct_from_environment(self, moduleName, verboseLogging=False):
        import senzing_module_config
        self.json_config = senzing_module_config.getJsonConfig()
        self.g2_handle = G2Diagnostic()
        return_code = self.g2_handle.init(moduleName, self.json_config, verboseLogging)

    def init_direct_with_config_id(self, configId):
        warnings.warn('init_direct_with_config_id does nothing for gRPC connections')
        return

    def reinit(self, configId):
        configId = bytes(configId, 'utf-8')
        self.g2_handle.reinit(configId)

    def destroy(self):
        self.g2_handle.destroy()

    # get sys into methods
    def get_physical_cores(self):
        return self.g2_handle.getPhysicalCores()

    def get_logical_cores(self):
        return self.g2_handle.getLogicalCores()

    def get_available_memory(self):
        return self.g2_handle.getAvailableMemory()

    def get_total_system_memory(self):
        return self.g2_handle.getTotalSystemMemory()

    def check_db_perf(self, secondsToRun, returnAsString=False):
        secondsToRun = int(secondsToRun)
        response = bytearray()
        self.g2_handle.checkDBPerf(secondsToRun, response=response)
        response = response.decode()
        if not returnAsString:
            response = json.loads(response)
        return response

    def get_db_info(self, returnAsString=False):
        response = bytearray()
        self.g2_handle.getDBInfo(response=response)
        response = response.decode()
        if not returnAsString:
            response = json.loads(response)
        return response

    # data query methods
    def get_entity_details(self, entityID, includeInternalFeatures=False, returnAsString=False):
        entityID = int(entityID)
        includeInternalFeatures = int(includeInternalFeatures)
        response = bytearray()
        self.g2_handle.getEntityDetails(entityID=entityID, includeInternalFeatures=includeInternalFeatures, response=response)

        #convert from bytebuffer to string
        response = response.decode()

        #maybe convert to dict
        if not returnAsString:
            response = json.loads(response)
        return response

    def get_relationship_details(self, relationshipID, includeInternalFeatures=False, returnAsString=False):
        relationshipID = int(relationshipID)
        includeInternalFeatures = int(includeInternalFeatures)
        response = bytearray()
        self.g2_handle.getRelationshipDetails(relationshipID=relationshipID, includeInternalFeatures=includeInternalFeatures, response=response)

        #convert from bytebuffer to string
        response = response.decode()

        #maybe convert to dict
        if not returnAsString:
            response = json.loads(response)
        return response

    def get_entity_resume(self, entityID, returnAsString=False):
        entityID = int(entityID)
        response = bytearray()
        self.g2_handle.getEntityResume(entityID=entityID, response=response)

        #convert from bytebuffer to string
        response = response.decode()

        #maybe convert to dict
        if not returnAsString:
            response = json.loads(response)
        return response

    def get_feature(self, libFeatID, returnAsString=False):
        libFeatID = int(libFeatID)
        response = bytearray()
        self.g2_handle.getFeature(libFeatID=libFeatID, response=response)

        #convert from bytebuffer to string
        response = response.decode()

        #maybe convert to dict
        if not returnAsString:
            response = json.loads(response)
        return response

    def find_entities_by_feature_ids(self, features, returnAsString=False):
        response = bytearray()
        self.g2_handle.findEntitiesByFeatureIDs(features=features, response=response)

        #convert from bytebuffer to string
        response = response.decode()

        #maybe convert to dict
        if not returnAsString:
            response = json.loads(response)
        return response

    def get_entity_list_by_size_request(self, entitySize):
        entitySize = int(entitySize)
        response = bytearray()
        handle = self.g2_handle.getEntityListBySize(entitySize=entitySize, response=response)
        print(response)

        return handle

    def fetch_next_entity_by_size(self, handle):
        fetch_data = bytearray()
        self.g2_handle.fetchNextEntityBySize(sizedEntityHandle=handle, response=fetch_data)
        if not fetch_data:
            return None
        return fetch_data.decode().strip()

    def close_entity_list_by_size(self, handle):
        return self.g2_handle.closeEntityListBySize(sizedEntityHandle=handle)

    def get_entity_list_by_size_return_list(self, entitySize):
        result_set = []
        handle = self.get_entity_list_by_size_request(entitySize=entitySize)

        while True:
            queried_entity = self.fetch_next_entity_by_size(handle=handle)
            if not queried_entity:
                break
            queried_entity = json.loads(queried_entity)
            result_set.extend(queried_entity)

        self.close_entity_list_by_size(handle=handle)
        return result_set

    def get_entity_list_by_size_with_callback(self, entitySize, callback):
        handle = self.get_entity_list_by_size_request(entitySize=entitySize)

        while True:
            queried_entity = self.fetch_next_entity_by_size(handle=handle)
            if not queried_entity:
                break
            callback(queried_entity)

        self.close_entity_list_by_size(handle=handle)

    # stats methods
    def get_entity_size_breakdown(self, minimumEntitySize, includeInternalFeatures=False, returnAsString=False):
        response = bytearray()
        self.g2_handle.getEntitySizeBreakdown(minimumEntitySize=minimumEntitySize, includeInternalFeatures=includeInternalFeatures, response=response)
        response = response.decode()
        if not returnAsString:
            response = json.loads(response)
        return response

    def get_data_source_counts(self, returnAsString=False):
        response = bytearray()
        self.g2_handle.getDataSourceCounts(response=response)
        response = response.decode()
        if not returnAsString:
            response = json.loads(response)
        return response

    def get_mapping_statistics(self, includeInternalFeatures=False, returnAsString=False):
        response = bytearray()
        self.g2_handle.getMappingStatistics(includeInternalFeatures=includeInternalFeatures, response=response)
        response = response.decode()
        if not returnAsString:
            response = json.loads(response)
        return response

    def get_resolution_statistics(self, returnAsString=False):
        response = bytearray()
        self.g2_handle.getResolutionStatistics(response=response)
        response = response.decode()
        if not returnAsString:
            response = json.loads(response)
        return response

    def get_generic_features(self, featureType, maximumEstimatedCount, returnAsString=False):
        response = bytearray()
        self.g2_handle.getGenericFeatures(featureType=featureType, maximumEstimatedCount=maximumEstimatedCount, response=response)
        response = response.decode()
        if not returnAsString:
            response = json.loads(response)
        return response

