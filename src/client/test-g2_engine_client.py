import sys
import unittest
import datetime
import g2_engine_client


class TestEngineAPI(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_smoketest_grpc(self):
        client = g2_engine_client.G2EngineClient()
        url = 'localhost:8258'
        client.init_grpc_connection_with_url(url=url)
        self.smoketest(client)

    def test_smoketest_direct(self):
        client = g2_engine_client.G2EngineClient()
        client.init_direct_from_environment('testing')
        self.smoketest(client)

    def smoketest(self, client):
        #first let's make sure the db is empty
        client.purge_repository()

        #should return a valid datetime
        print('\n')
        response = client.get_repository_last_modified_time()
        print(response)
        self.assertIsInstance(response, datetime.datetime)
        self.assertRegex(str(response), '(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})\.(\d{6})')

        #add a record -- no response expected
        datasource_code = 'TEST'
        record_id = '1001'
        example_record = {"ADDR_LINE1":"123 Main Street, Las Vegas NV 89132","ADDR_TYPE":"MAILING","AMOUNT":"100","DATE":"1/2/18","DATE_OF_BIRTH":"12/11/1978","EMAIL_ADDRESS":"bsmith@work.com","PHONE_NUMBER":"702-919-1300","PHONE_TYPE":"HOME","PRIMARY_NAME_FIRST":"Robert","PRIMARY_NAME_LAST":"Smith","RECORD_TYPE":"PERSON","STATUS":"Active"}
        load_id = 'Add Record CUSTOMERS 1001'
        client.add_record(datasource_code, record_id, example_record, load_id)

        datasource_code = 'TEST'
        record_id = '1002'
        example_record = {"ADDR_LINE1":"123 Main Street, Las Vegas NV 89132","ADDR_TYPE":"MAILING","AMOUNT":"100","DATE":"1/2/18","DATE_OF_BIRTH":"12/11/1978","EMAIL_ADDRESS":"bsmith@work.com","PHONE_NUMBER":"702-919-1300","PHONE_TYPE":"HOME","PRIMARY_NAME_FIRST":"Rob","PRIMARY_NAME_LAST":"Smith","RECORD_TYPE":"PERSON","STATUS":"Active"}
        load_id = 'Add Record CUSTOMERS 1002'
        info = client.add_record_with_info(datasource_code, record_id, example_record, load_id)
        #validate the record_id and datasource
        self.assertIsInstance(info, dict)
        self.assertEqual(info['DATA_SOURCE'], 'TEST')
        self.assertEqual(info['RECORD_ID'], '1002')

        datasource_code = 'TEST'
        example_record = {"ADDR_LINE1":"321 Commerce Street, Las Vegas NV 89101","ADDR_TYPE":"MAILING","AMOUNT":"100","DATE":"1/2/18","DATE_OF_BIRTH":"12/11/1978","EMAIL_ADDRESS":"bsmith@work.com","PHONE_NUMBER":"702-919-1300","PHONE_TYPE":"HOME","PRIMARY_NAME_FIRST":"Bob","PRIMARY_NAME_LAST":"Smith","RECORD_TYPE":"PERSON","STATUS":"Active"}
        load_id = 'Add Record CUSTOMERS 1003'
        record_id = client.add_record_with_returned_record_id(
            datasource_code=datasource_code,
            data_as_json=example_record,
            load_id=load_id)
        #response should be a sha-1 hash
        self.assertIsInstance(record_id, str)
        self.assertEqual(len(record_id), 40)

        datasource_code = 'TEST'
        example_record = {"ADDR_LINE1":"123 Commerce Street, Las Vegas NV 89101","ADDR_TYPE":"MAILING","AMOUNT":"100","DATE":"1/2/18","DATE_OF_BIRTH":"12/11/1978","EMAIL_ADDRESS":"bsmith@work.com","PHONE_NUMBER":"702-919-1300","PHONE_TYPE":"HOME","PRIMARY_NAME_FIRST":"Robert","PRIMARY_NAME_LAST":"Smith","RECORD_TYPE":"PERSON","STATUS":"Active"}
        load_id = 'Add Record CUSTOMERS 1004'
        (info, record_id) = client.add_record_with_info_with_returned_record_id(
            datasource_code=datasource_code,
            data_as_json=example_record,
            load_id=load_id)
        #response should be a sha-1 hash
        print(info)
        self.assertIsInstance(info, dict)
        self.assertIsInstance(record_id, str)
        self.assertEqual(len(record_id), 40)
        self.assertEqual(info['DATA_SOURCE'], 'TEST')
        self.assertEqual(info['AFFECTED_ENTITIES'][0]['ENTITY_ID'], 1)




if __name__ == '__main__':
    unittest.main()
