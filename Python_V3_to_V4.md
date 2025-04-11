# Python SDK V3 to V4  Migration

This document outlines fundamental changes and differences for the Senzing V4 Python SDK to guide you as a developer. Although there are numerous changes to the Senzing V4 SDKs, migrating your Python applications and services is straight forward. The changes will simplify your code, align to Python standards, and improve aspects like IDE IntelliSense.

If you haven't already, start with [breaking changes][breaking-changes]. This covers additional details not specifically related to Python such as hardware, software, overall SDK changes, and database schema changes.

## G2 Becomes Sz

In the V3 SDK, Python artifacts such as modules, classes, exceptions and tools used the term G2; a code name for the main Senzing engine. This is typically observed as a prefix to the aforementioned artifacts.

Senzing V4 has, for the most part, replaced G2 with the term SZ, Sz, or sz depending on the context. You may still notice G2 used in some of the overall product files, but the V4 SDK Python artifacts have replaced G2 with a variant of SZ. A couple of examples of such changes:

- Python SDK module naming, G2 is replaced with sz in V4
  - G2Engine.py changes to szengine.py

- Exceptions, G2 is replaced with Sz (and Error) in V4
  - G2Exception changes to SzError

- Engine flags, G2 is replaced with SZ in V4
  - G2_ENTITY_DEFAULT_FLAGS changes to SZ_ENTITY_DEFAULT_FLAGS

## Modules Structure

The V3 Python SDK modules are located in a single path for the product at `/opt/senzing/g2/sdk/python/senzing/` (or a project `<project_path>/sdk/python/senzing/`). These modules contain concrete classes and methods for working with the Python SDK.

There are 2 paths for the V4 Python SDK modules, considering the product install path:

1. `/opt/senzing/er/sdk/python/senzing/`
    - Non-instantiable abstract base classes and constants for unifying the method signatures of concrete implementations, such as senzing_core below
1. `/opt/senzing/er/sdk/python/senzing_core/`
    - Instantiable concrete classes for working with the Python SDK

Python doesn't have interfaces similar to other languages, using abstract base classes in this manner achieves similar functionality. The module classes in `senzing_core` inherit from the `senzing` module classes, ensuring the required methods and signatures are implemented. [sz-sdk-python-grpc](https://github.com/senzing-garage/sz-sdk-python-grpc) is an example of another implementation using the `senzing` abstract base classes.

## Moving Towards Creational Patterns

Using the V3 SDK, engine objects are instantiated and then initialized with `init()`, passing in arguments to identify the instance, engine configuration settings, and whether to use debug tracing. G2Diagnostic, G2Engine, and G2Product example initialization code might look like:

```python
try:
    g2_diagnostic = G2Diagnostic()
    g2_diagnostic.init('example', engine_config, False)
    g2_engine = G2Engine()
    g2_engine.init('example', engine_config, False)
    g2_product = G2Product()
    g2_product.init('example', engine_config, False)
except G2Exception as err:
    print(f"\n{err.__class__.__name__} - {err}")
```

The V4 SDK uses an abstract factory pattern for the creation and initialization of Senzing engine objects. The abstract factory is instantiated with the required configuration settings. Subsequent engine objects requested from the abstract factory use the same single set of configuration settings. This simplifies instantiation of Senzing engines and removes the possibility of inadvertently introducing configuration errors. The same code for V4:

```python
try:
    sz_factory = SzAbstractFactoryCore('example', engine_config, False)
    sz_diagnostic = sz_factory.create_diagnostic()
    sz_engine = sz_factory.create_engine()
    sz_product = sz_factory.create_product()
except SzError as err:
    print(f"\n{err.__class__.__name__} - {err}")
```

## Method Response Assignment

Gone is allocating a byte array to return method responses to. Prior to V4, the Senzing engine returned a return code to the Python SDK method. If the return code was non-zero the error details were requested from the engine, converted to a Python Senzing exception with the error details and raised. As the SDK method was collecting the return code, byte arrays were used in the V3 SDK to assign successful responses to.

```python
try:
    response = bytearray()
    g2_engine.searchByAttributes(
        record_json_str,
        response,
        G2EngineFlags.G2_SEARCH_BY_ATTRIBUTES_MINIMAL_ALL,
    )
except G2Exception as err:
    print(f"\n{err.__class__.__name__} - {err}")
print(response.decode())
```

This has been improved in V4, allowing the V4 SDK to access the return code separately from responses. Responses are now returned directly as types such as `str` and `int` in V4.

```python
try:
    response = sz_engine.searchByAttributes(record_json_str, SzEngineFlags.SZ_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS)
except SzError as err:
    print(f"\n{err.__class__.__name__} - {err}")
print(response)
```

## With Info Methods {#with-info}

The V3 SDK provides "with info" methods to request a response for methods that perform adding, deleting, processing, and reevaluating. For example, `addRecord()` is used to add a record, and `addRecordWithInfo()` to add a record and return a response outlining any affected entities from the add operation.

```python
g2_engine.addRecord("TEST", "78720B", record_json_str)
```

```python
response = bytearray()
g2_engine.addRecordWithInfo("TEST", "78720B", record_json_str, response)
print(response)
```

The separate `WithInfo` methods have been removed in the V4 SDK, the capability is now included in the `add_record()`, `delete_record`, `process_redo_record()`,`reevaluate_entity()`, and `reevaluate_record()` methods. Requesting the with info response is achieved with the use of the optional `flags` argument specifying `SZ_WITH_INFO`. The default is not to return the with info response, in which case an empty string is returned.

```python
_ = sz_engine.add_record("TEST", "78720B", record_json_str)
```

Return the with info response using the `flags` argument.

```python
response = sz_engine.add_record("TEST", "78720B", record_json_str, flags=SzEngineFlags.SZ_WITH_INFO)
print(response)
```

## Processing Redo Records

Methods for fetching and processing redo records have changed. In the V3 SDK, `getRedoRecord()` is used to fetch a redo record (if any are available) and `process()` to request handling of the redo record. `process()` is really an internal method, it could handle redo and other record types the Senzing engine understands. A simple example to process redo records:

```python
white True:
    redo_record = bytearray()
    g2_engine.getRedoRecord(redo_record)
    if not redo_record:
        time.sleep(30)
        continue
    g2_engine.process(redo_record.decode())
```

To achieve the same in the V4 SDK the methods are now `get_redo_record()` and `process_redo_record()`.

```python
white True:
    redo_record = sz_engine.get_redo_record()
    if not redo_record:
        time.sleep(30)
        continue
    sz_engine.process_redo_record(redo_record)
```

## JSON String Arguments

A number of methods take a JSON string argument in the V3 SDK to describe entities, records, or data sources. For example, `findNetworkByRecordID()` has the argument `recordList` to specify the data sources and record IDs to find paths between and networks around.

```python
response = bytearray()
g2_engine.findNetworkByRecordID(
    {
        "RECORDS":[
            {"DATA_SOURCE":"CUSTOMERS","RECORD_ID":"1001"},
            {"DATA_SOURCE":"WATCHLIST","RECORD_ID":"1007"}, 
            {"DATA_SOURCE":"WATCHLIST","RECORD_ID":"1010"},
        ]
    },
    6,
    4,
    5,
    response
)
```

You no longer need to construct the JSON string for similar arguments in the V4 SDK. The equivalent method in V4 `find_network_by_record_id()` accepts a list of tuples, each consisting of 2 strings. The first string represents the data source, the second the record ID.

```python
response = sz_engine.findNetworkByRecordID([("CUSTOMERS", "1001"), ("WATCHLIST", "1007"), ("WATCHLIST", "1010")], 6, 4, 5)
```

These are the methods in the V4 Python SDK with arguments no longer requiring a JSON string, instead accepting data structures to provide the information.

| Module | Method | Argument | Type | Values |
| ------ | ------ | -------- | ---- | ------ |
| szconfig | add_data_source | data_source_code | str | Data source |
|  | delete_data_source | data_source_code | str | Data source |
| szengine | find_network_by_entity_id | entity_ids | [int, ...] | Entity ID(s) |
|  | find_network_by_record_id | record_keys | [(str, str), ...] | Data source, Record ID |
|  | find_path_by_entity_id | avoid_entity_ids | [int, ...] | Entity ID(s) |
|  |  | required_data_sources | [str, ...] | Data Source(s) |
|  | find_path_by_record_id | avoid_record_keys | [(str, str), ...] | Data source, Record ID |
|  |  | required_data_sources | [str, ...] | Data Source(s) |
| | get_virtual_entity_by_record_id | record_keys | [(str, str), ...] | Data source, Record ID |

## Less is more

In addition to the `with info` methods [being removed in V4](#with-info) other methods have been collapsed into fewer methods; such as for find path. There are six methods in the V3 SDK for find path, three for finding paths by entity IDs and three for finding paths by record IDs. You would choose one depending on if you were interested in excluding entities/records in the path or finding paths that contain specific data sources.

- `findPathByEntityID()`
- `findPathByRecordID()`
- `findPathExcludingByEntityID()`
- `findPathExcludingByRecordID()`
- `findPathIncludingSourceByEntityID()`
- `findPathIncludingSourceByRecordID()`

There are now 2 methods in the V4 SDK, one for using entity IDs, the other using record IDs.

- `find_path_by_entity_id()`
- `find_path_by_record_id()`

The V4 SDK methods take optional arguments for avoiding specific entities/records, and/or the path having specific data sources along it.

### findPathByEntityID() ->  find_path_by_entity_id()

#### findPathByEntityID()

```python
response = bytearray()
g2_engine.findPathByEntityId(787, 201123, 3, response)
```

#### find_path_by_entity_id()

```python
response = sz_engine.find_path_by_entity_id(787, 201123, 3)
```

### findPathExcludingByEntityID() -> find_path_by_entity_id()

#### findPathExcludingByEntityID()

```python
response = bytearray()
g2_engine.findPathExcludingByEntityID(787, 201123, 3, '{"ENTITIES": [{"ENTITY_ID": 1}, {"ENTITY_ID": 100002}]}', response)
```

#### find_path_by_entity_id()

```python
response = sz_engine.find_path_by_entity_id(787, 201123, 3, [1, 100002])
```

### findPathIncludingSourceByEntityID() -> find_path_by_entity_id()

#### findPathIncludingSourceByEntityID()

```python
response = bytearray()
g2_engine.findPathIncludingSourceByEntityID(787, 201123, 3, '', '{"DATA_SOURCES": ["REFERENCE", "CUSTOMERS"]}', response)
```

#### find_path_by_entity_id()

```python
response = sz_engine.find_path_by_entity_id(787, 201123, 3, required_data_sources = ["REFERENCE", "CUSTOMERS"])
```

Note, in these examples a blank is used for `findPathIncludingSourceByEntityID()` and a named argument for `find_path_by_entity_id()`. When requesting specific data sources, entity IDs to avoid can optionally be specified.

## Changes to config and configmgr ***

*** TODO Add

## Code Snippets

- [V4 Python Code Snippets](https://github.com/Senzing/code-snippets-v4/tree/main/python)

## Additional Differences

These are Python specific not covered in [breaking changes][breaking-changes]. The tables don't outline every change, only those that are new or continue to exist in the V4 SDK. For a full list of changes see [breaking changes][breaking-changes]. A blank entry in the V3 column and a value in the V4 column denotes added in V4.

### Modules

| V3 | V4 |
| --- | --- |
| G2Config.py | szconfig.py |
| G2ConfigMgr.py | szconfigmanager.py |
| G2Diagnostic.py | szdiagnostic.py |
| G2Engine.py | szengine.py |
| G2EngineFlags.py | szengineflags.py *|
| G2Exception.py | szerror.py * |
| G2Product.py | szproduct.py |

\* These modules are abstract base classes located in sdk/python/senzing/

### Method Names

#### G2Config.py -> szconfig *** TODO

| V3  | V4 |
| --- | --- |
| addDataSource | add_data_source |
| close | close_config |
| create | create_config |
| deleteDataSource | delete_data_source |
| listDataSources | get_data_sources |
| save | export |

#### G2ConfigMgr.py -> szconfigmanager *** TODO

| V3  | V4 |
| --- | --- |
| addConfig |  |
| clearLastException |  |
| destroy |  |
| getConfig |  |
| getConfigList |  |
| getDefaultConfigID |  |
| getLastException |  |
| getLastExceptionCode |  |
| init |  |
| replaceDefaultConfigID |  |
| setDefaultConfigID |  |

#### G2Diagnostic.py -> szdiagnostic

| V3  | V4 |
| --- | --- |
| checkDBPerf | check_datastore_performance |
| getDBInfo | get_datastore_info |
| | purge_repository |

#### G2Engine.py -> szengine

| V3  | V4 |
| --- | --- |
| addRecord | add_record |
| closeExport | close_export |
| countRedoRecords | count_redo_records |
| deleteRecord | delete_record |
| exportCSVEntityReport | export_csv_entity_report |
| exportJSONEntityReport | export_json_entity_report |
| fetchNext | fetch_next |
| findInterestingEntitiesByEntityID | find_interesting_entities_by_entity_id |
| findInterestingEntitiesByRecordID | find_interesting_entities_by_record_id |
| findNetworkByEntityID | find_network_by_entity_id |
| findNetworkByRecordID | find_network_by_record_id |
| findPathByEntityID | find_path_by_entity_id |
| findPathByRecordID | find_path_by_record_id |
| getActiveConfigID | get_active_config_id |
| getEntityByEntityID | get_entity_by_entity_id |
| getEntityByRecordID | get_entity_by_record_id |
| getRecord | get_record |
| getRedoRecord | get_redo_record |
| getVirtualEntityByRecordID | get_virtual_entity_by_record_id |
| howEntityByEntityID | how_entity_by_entity_id |
| primeEngine | prime_engine |
| | preprocess_record |
| processRedoRecord | process_redo_record |
| reevaluateEntity | reevaluate_entity |
| reevaluateRecord | reevaluate_record |
| searchByAttributes | search_by_attributes |
| stats | get_stats |
| whyEntities | why_entities |
| whyRecords | why_records |
| | why_record_in_entity |

#### G2Product.py -> szproduct

| V3  | V4 |
| --- | --- |
| license | get_license |
| version | get_version |

### Exceptions

| V3 | V4 |
| --- | --- |
| G2BadInputException | SzBadInputError |
| G2ConfigurationException | SzConfigurationError |
| G2DatabaseConnectionLostException | SzDatabaseConnectionLostError |
| G2DatabaseException | SzDatabaseError |
|  | SzDatabaseTransientError |
| G2Exception | SzError |
|  | SzGeneralError |
| G2LicenseException | SzLicenseError |
| G2NotInitializedException | SzNotInitializedError |
| G2NotFoundException | SzNotFoundError |
|  | SzReplaceConflictError |
| G2RetryableException | SzRetryableError |
|  | SzSdkError |
| G2RetryTimeoutExceededException | SzRetryTimeoutExceededError |
| G2UnhandledException | SzUnhandledError |
| G2UnknownDatasourceException | SzUnknownDataSourceError |
| G2UnrecoverableException | SzUnrecoverableError |

[breaking-changes]: https://senzing.com/docs/4_beta/4_0_breaking_changes/index.html
