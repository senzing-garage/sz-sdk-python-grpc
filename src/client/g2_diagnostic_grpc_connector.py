import grpc
import sys
import json
import warnings

sys.path.insert(0, '/home/gadair/servegrpc/protobuf/g2diagnostic')

import g2diagnostic_pb2_grpc
import g2diagnostic_pb2

class G2DiagnosticGRPCConnector:
    def __init__(self):
        self.channel = None
        self.stub = None

    # startup/shutdown methods

    #GGANOTE: depricate when server configs itself
    def init(self, url, moduleName, iniParams, verboseLogging=False):
        self.channel = grpc.insecure_channel(url)
        self.stub = g2diagnostic_pb2_grpc.G2DiagnosticStub(self.channel)

        if isinstance(iniParams,dict):
            iniParams = json.dumps(iniParams)

        req = g2diagnostic_pb2.InitRequest(moduleName=moduleName, iniParams=iniParams, verboseLogging=verboseLogging)
        #req = g2diagnostic_pb2.InitRequest(moduleName=moduleName, iniParams=iniParams, verboseLogging=verboseLogging)
        return self.stub.Init(req)

    def init_with_url(self, url):
        self.channel = grpc.insecure_channel(url)
        self.stub = g2diagnostic_pb2_grpc.G2DiagnosticStub(self.channel)
        # add a ping here or something to ensure it connected

    def init_direct_with_config_id(self, configId):
        warnings.warn('init_direct_with_config_id does nothing for gRPC connections')
        return

    def reinit(self, configId):
        warnings.warn('reinit does nothing for gRPC connections')
        return

    def destroy(self):
        return self.stub.Destroy(g2diagnostic_pb2.DestroyRequest())
#        warnings.warn("destroy does nothing for gRPC connections ")
#        return 

    # get sys into methods
    def get_physical_cores(self):
        return self.stub.GetPhysicalCores(g2diagnostic_pb2.GetPhysicalCoresRequest())

    def get_logical_cores(self):
        return self.stub.GetLogicalCores(g2diagnostic_pb2.GetLogicalCoresRequest())

    def get_available_memory(self):
        return self.stub.GetAvailableMemory(g2diagnostic_pb2.GetAvailableMemoryRequest())

    def get_total_system_memory(self):
        return self.stub.GetTotalSystemMemory(g2diagnostic_pb2.GetTotalSystemMemoryRequest())

    def check_db_perf(self, secondsToRun):
        secondsToRun = int(secondsToRun)
        return self.stub.CheckDBPerf(g2diagnostic_pb2.CheckDBPerfRequest(secondsToRun=secondsToRun))

    def get_db_info(self):
        return self.stub.GetDBInfo(g2diagnostic_pb2.GetDBInfoRequest())

    # data query methods
    def get_entity_details(self, entityID, includeInternalFeatures=False):
        entityID = int(entityID)
        includeInternalFeatures = int(includeInternalFeatures)
        return self.stub.GetEntityDetails(g2diagnostic_pb2.GetEntityDetailsRequest(entityID=entityID, includeInternalFeatures=includeInternalFeatures))

    def get_relationship_details(self, relationshipID, includeInternalFeatures=False):
        relationshipID = int(relationshipID)
        includeInternalFeatures = int(includeInternalFeatures)
        return self.stub.GetRelationshipDetails(g2diagnostic_pb2.GetRelationshipDetailsRequest(relationshipID=relationshipID, includeInternalFeatures=includeInternalFeatures))

    def get_entity_resume(self, entityID):
        entityID = int(entityID)
        return self.stub.GetEntityResume(g2diagnostic_pb2.GetEntityResumeRequest(entityID=entityID))

    def get_feature(self, libFeatID):
        libFeatID = int(libFeatID)
        return self.stub.GetFeature(g2diagnostic_pb2.GetFeatureRequest(libFeatID=libFeatID))

    def find_entities_by_feature_ids(self, features):
        if isinstance(features, int):
            features = str(int)
        if isinstance(features, (list, tuple)) == False:
            features = [features]
        features = json.dumps(features)
        return self.stub.FindEntitiesByFeatureIDs(g2diagnostic_pb2.FindEntitiesByFeatureIDsRequest(features=features))

    def get_entity_list_by_size_request(self, entitySize):
        entitySize = int(entitySize)
        return self.stub.GetEntityListBySize(g2diagnostic_pb2.GetEntityListBySizeRequest(entitySize=entitySize))

    def fetch_next_entity_by_size(self, handle):
        return self.stub.FetchNextEntityBySize(g2diagnostic_pb2.FetchNextEntityBySizeRequest(handle))

    def close_entity_list_by_size(self, handle):
        return self.stub.CloseEntityListBySize(g2diagnostic_pb2.CloseEntityListBySizeRequest(handle))

    # stats methods
    def get_entity_size_breakdown(self, minimumEntitySize, includeInternalFeatures=False):
        return self.stub.GetEntitySizeBreakdown(g2diagnostic_pb2.GetEntitySizeBreakdownRequest(minimumEntitySize=minimumEntitySize, includeInternalFeatures=includeInternalFeatures))

    def get_data_source_counts(self):
        return self.stub.GetDataSourceCounts(g2diagnostic_pb2.GetDataSourceCountsRequest())

    def get_mapping_statistics(self, includeInternalFeatures=False):
        return self.stub.GetMappingStatistics(g2diagnostic_pb2.GetMappingStatisticsRequest(includeInternalFeatures=includeInternalFeatures))

    def get_resolution_statistics(self):
        return self.stub.GetResolutionStatistics(g2diagnostic_pb2.GetResolutionStatisticsRequest())

    def get_generic_features(self, featureType, maximumEstimatedCount):
        return self.stub.GetGenericFeatures(g2diagnostic_pb2.GetGenericFeaturesRequest(featureType=featureType, maximumEstimatedCount=maximumEstimatedCount))
