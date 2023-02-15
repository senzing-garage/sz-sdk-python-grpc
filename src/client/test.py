import g2_diagnostic_client


def do_tests(client):
    def my_callback(entity):
        print(entity)
        print(type(entity))

    print('get_entity_list_by_size_with_callback')
    response = client.get_entity_list_by_size_with_callback(2, my_callback)
    print(response)

    print('get_entity_list_by_size_return_list')
    response = client.get_entity_list_by_size_return_list(2)
    print(response)

    print('GetEntityDetails')
    response = client.get_entity_details(1, False)
    print(response)
    response = client.get_entity_details(1, True)
    print(response)

    print('GetRelationshipDetails')
    response = client.get_relationship_details(59, False)
    print(response)
    response = client.get_relationship_details(59, True)
    print(response)

    print('GetEntityResumeRequest')
    response = client.get_entity_resume(1)
    print(response)

    print('GetFeature')
    response = client.get_feature(1)
    print(response)

    print('FindEntitiesByFeatureIDs')
    print('skipping for now')
#    response=client.find_entities_by_feature_ids([1,2,3])
#    print(response)

    print('GetEntitySizeBreakdown')
    response = client.get_enity_size_breakdown(minimum_entity_size=2, include_internal_features=False)
    print(response)
    response = client.get_enity_size_breakdown(minimum_entity_size=2, include_internal_features=True)
    print(response)

    print('GetDataSourceCounts')
    response = client.get_data_source_counts()
    print(response)

    print('GetMappingStatistics')
    response = client.get_mapping_statistics()
    print(response)

    print('GetResolutionStatistics')
    response = client.get_resolution_statistics()
    print(response)

    print('GetGenericFeatures')
    response = client.get_generic_features('NAME', 1000000)
    print(response)

    print('GetDBInfo')
    response = client.get_db_info()
    print(response)

    print('getPhysicalCores')
    response = client.get_physical_cores()
    print(response)

    print('getAvailableMemory')
    response = client.get_available_memory()
    print(response)

    print('getTotalSystemMemory')
    response = client.get_total_system_memory()
    print(response)

    print('getLogicalCores')
    response = client.get_logical_cores()
    print(response)

    print('CheckDBPerf')
    response = client.check_db_perf(10)
    print(response)

    print('Destroy')
    response = client.destroy()
    print(response)




if __name__ == "__main__":
    INI_PARAMS = {"PIPELINE"  :
                  {
                      "CONFIGPATH":"/home/gadair/senzing/etc",
                      "RESOURCEPATH":"/opt/senzing/g2/resources",
                      "SUPPORTPATH":"/opt/senzing/data/3.0.0"
                  },
                  "SQL":
                  {
                      "CONNECTION":"sqlite3://na:na@/home/gadair/senzing/var/sqlite/G2C.db"
                  }
                 }

    CLIENT = g2_diagnostic_client.G2DiagnosticClient()
    print('init')
    URL = 'localhost:8258'
    #RESPONSE = client.init_grpc_connection_with_url(url)

    #run grpc
    RESPONSE = CLIENT.init_grpc_connection_with_url(url=URL)
    #RESPONSE = CLIENT.legacy_init_grpc_connector(url=URL, module_name='grpc_test', ini_params=INI_PARAMS)
    print(RESPONSE)
    do_tests(CLIENT)

    #run direct
    RESPONSE = CLIENT.init_direct_from_environment(module_name='grpc_test')
    do_tests(CLIENT)
