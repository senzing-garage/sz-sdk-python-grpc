import g2_engine_client


def do_tests(client):
    print('export_json_entity_report_iteritems')
    for item in client.export_json_entity_report_iteritems():
        print(item)
    return

    print('get_active_config_id')
    response = client.get_active_config_id()
    print(type(response))
    print(response)

    print('export_config')
    response = client.export_config()
    print(type(response))
    print(response)

    print('export_config_and_config_id')
    (config,config_id) = client.export_config_and_config_id()
    print(type(config))
    print(config)
    print(type(config_id))
    print(config_id)

    print('get_respository_last_modified_time')
    response = client.get_repository_last_modified_time()
    print(type(response))
    print(response)

    print('add_record')
    datasource_code = 'TEST'
    record_id = '1001'
    example_record = {"ADDR_LINE1":"123 Main Street, Las Vegas NV 89132","ADDR_TYPE":"MAILING","AMOUNT":"100","DATE":"1/2/18","DATE_OF_BIRTH":"12/11/1978","EMAIL_ADDRESS":"bsmith@work.com","PHONE_NUMBER":"702-919-1300","PHONE_TYPE":"HOME","PRIMARY_NAME_FIRST":"Robert","PRIMARY_NAME_LAST":"Smith","RECORD_TYPE":"PERSON","STATUS":"Active"}
    load_id = 'Add Record CUSTOMERS 1001'
    client.add_record(datasource_code, record_id, example_record, load_id)

    print('add_record_with_info')
    datasource_code = 'TEST'
    record_id = '1002'
    example_record = {"ADDR_LINE1":"123 Main Street, Las Vegas NV 89132","ADDR_TYPE":"MAILING","AMOUNT":"100","DATE":"1/2/18","DATE_OF_BIRTH":"12/11/1978","EMAIL_ADDRESS":"bsmith@work.com","PHONE_NUMBER":"702-919-1300","PHONE_TYPE":"HOME","PRIMARY_NAME_FIRST":"Robert","PRIMARY_NAME_LAST":"Smith","RECORD_TYPE":"PERSON","STATUS":"Active"}
    load_id = 'Add Record CUSTOMERS 1002'
    response = client.add_record_with_info(datasource_code, record_id, example_record, load_id)
    print(response)

    print('add_record_with_returned_record_id')
    datasource_code = 'TEST'
    example_record = {"ADDR_LINE1":"123 Main Street, Las Vegas NV 89132","ADDR_TYPE":"MAILING","AMOUNT":"100","DATE":"1/2/18","DATE_OF_BIRTH":"12/11/1978","EMAIL_ADDRESS":"bsmith@work.com","PHONE_NUMBER":"702-919-1300","PHONE_TYPE":"HOME","PRIMARY_NAME_FIRST":"Robert","PRIMARY_NAME_LAST":"Smith","RECORD_TYPE":"PERSON","STATUS":"Active"}
    load_id = 'Add Record CUSTOMERS 1003'
    response = client.add_record_with_returned_record_id(datasource_code, example_record, load_id)
    print(response)

    print('add_record_with_info_with_returned_record_id')
    datasource_code = 'TEST'
    example_record = {"ADDR_LINE1":"123 Main Street, Las Vegas NV 89132","ADDR_TYPE":"MAILING","AMOUNT":"100","DATE":"1/2/18","DATE_OF_BIRTH":"12/11/1978","EMAIL_ADDRESS":"bsmith@work.com","PHONE_NUMBER":"702-919-1300","PHONE_TYPE":"HOME","PRIMARY_NAME_FIRST":"Robert","PRIMARY_NAME_LAST":"Smith","RECORD_TYPE":"PERSON","STATUS":"Active"}
    load_id = 'Add Record CUSTOMERS 1004'
    response = client.add_record_with_info_with_returned_record_id(datasource_code, example_record, load_id)
    print(response)

    print('replace_record')
    datasource_code = 'TEST'
    record_id = '1005'
    example_record = {"ADDR_LINE1":"123 Main Street, Las Vegas NV 89132","ADDR_TYPE":"MAILING","AMOUNT":"100","DATE":"1/2/18","DATE_OF_BIRTH":"12/11/1978","EMAIL_ADDRESS":"bsmith@work.com","PHONE_NUMBER":"702-919-1300","PHONE_TYPE":"HOME","PRIMARY_NAME_FIRST":"Robert","PRIMARY_NAME_LAST":"Smith","RECORD_TYPE":"PERSON","STATUS":"Active"}
    load_id = 'Replace Record CUSTOMERS 1005'
    client.replace_record(datasource_code, record_id, example_record, load_id)

    print('reaplce_record_with_info')
    datasource_code = 'TEST'
    record_id = '1006'
    example_record = {"ADDR_LINE1":"123 Main Street, Las Vegas NV 89132","ADDR_TYPE":"MAILING","AMOUNT":"100","DATE":"1/2/18","DATE_OF_BIRTH":"12/11/1978","EMAIL_ADDRESS":"bsmith@work.com","PHONE_NUMBER":"702-919-1300","PHONE_TYPE":"HOME","PRIMARY_NAME_FIRST":"Robert","PRIMARY_NAME_LAST":"Smith","RECORD_TYPE":"PERSON","STATUS":"Active"}
    load_id = 'Add Record CUSTOMERS 1006'
    response = client.add_record_with_info(datasource_code, record_id, example_record, load_id)
    print(response)

    print('reevaluate_record')
    client.reevaluate_record('TEST','1001')

    print('reevaluate_record_with_info')
    response = client.reevaluate_record_with_info('TEST','1001')
    print(response)

    print('count_redo_records')
    response = client.count_redo_records()
    print(response)
    print('count_redo_records done')

    print('get_redo_record')
    response = client.get_redo_record()
    print(response)
    print('get_redo_record done')





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

    CLIENT = g2_engine_client.G2EngineClient()
    URL = 'localhost:8258'

    #run grpc
    print('init')
    RESPONSE = CLIENT.init_grpc_connection_with_url(url=URL)
    print(RESPONSE)
    print('prime_engine')
    RESPONSE = CLIENT.prime_engine()
    print(RESPONSE)

    do_tests(CLIENT)

    #run direct
#    RESPONSE = CLIENT.init_direct_from_environment(module_name='grpc_test')
#    do_tests(CLIENT)
