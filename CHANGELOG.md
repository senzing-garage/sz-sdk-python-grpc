# Changelog

All notable changes to this project will be documented in this file.

The changelog format is based on [Keep a Changelog] and [CommonMark].
This project adheres to [Semantic Versioning].

## [Unreleased]

## [0.5.14] - 2025-09-15

### Fixed in 0.5.14

- Pylint failure with updated pylint-per-file-ignores

## [0.5.13] - 2025-07-23

### Changed in 0.5.13

- Update dependencies

## [0.5.12] - 2025-07-23

### Changed in 0.5.12

- Sync with `sz-sdk-python-core`

## [0.5.11] - 2025-07-16

### Changed in 0.5.11

- Added `SzAbstractFactory.Destroy()`

## [0.5.10] - 2025-07-09

### Changed in 0.5.10

- Change `SzConfig.add_data_source` to `SzConfig.register_data_source`
- Change `SzConfig.delete_data_source` to `SzConfig.unregister_data_source`
- Change `SzConfig.get_data_sources` to `SzConfig.get_data_source_registry`
- Change `SzDiagnostic.check_datastore_performance` to `SzDiagnostic.check_repository_performance`
- Change `SzDiagnostic.get_datastore_info` to `SzDiagnostic.get_repository_info`
- Change `SzEngine.close_export` to `SzEngine.close_export_report`
- Change `SzEngine.preprocess_record` to ``SzEngine.get_record_preview`

## [0.5.9] - 2025-07-07

### Changed in 0.5.9

- Update dependencies

## [0.5.8] - 2025-06-18

### Changed in 0.5.8

- szconfigmanager.get_configs changed to szconfigmanager.get_config_registry

### Fixed in 0.5.8

- Example output for preprocess_record updated

## [0.5.7] - 2025-06-13

### Added in 0.5.7

- New tests for szconfig

### Changed in 0.5.7

- Examples cleanup
- Lowered sphinx-tabs version to 3.4.5 due to dependency issue with sphinx-toolbox currently
- Some method definitions now use new default flags instead of integer values in szengine.py
- SZ_NO_FLAGS is now defined in the abstract for szengineflags.py and no longer in constants.py

### Fixed in 0.5.7

- Change preprocess_record and example to use SZ_PREPROCESS_RECORD_DEFAULT_FLAGS

## [0.5.6] - 2025-05-12

### Removed in 0.5.6

- Examples/misc flags_by_name and flags_by_value

### Fixed in 0.5.6

- Corrected flags for examples, why_record_in_entity.py and why_records.py

## [0.5.5] - 2025-04-21

### Changed in 0.5.5

- Simplify and clean up examples

## [0.5.4] - 2025-04-16

### Added in 0.5.4

- `SzEngine.why_search`

## [0.5.3] - 2025-04-11

### Added in 0.5.3

- Restructure `SzConfig` and `SzConfigManager`

## [0.5.2] - 2025-03-21

### Added in 0.5.2

- TLS pass phrase support

## [0.5.1] - 2025-03-18

### Added in 0.5.1

- Mutual TLS support

## [0.5.0] - 2025-02-24

### Added in 0.5.0

- Server-side TLS support

## [0.4.4] - 2025-02-12

### Changed in 0.4.4

- Update Protobuf files

## [0.4.3] - 2025-02-10

### Changed in 0.4.3

- Update gRPC

## [0.4.2] - 2025-01-31

### Changed in 0.4.2

- Improve testcases

## [0.4.1] - 2025-01-29

### Changed in 0.4.1

- Sync with `sz-sdk-python-core`
- Update examples

## [0.4.0] - 2025-01-10

### Changed in 0.4.0

- Rename class names.  Example: from `SzAbstractFactory` to `SzAbstractFactoryGrpc`

## [0.3.8] - 2024-12-04

### Added in 0.3.8

- `senzing` package dependency

### Deleted in 0.3.8

- `senzing-abstract` package dependency

## [0.3.7] - 2024-12-03

### Changed in 0.3.7

- Sync with sz-sdk-python-core

## [0.3.6] - 2024-12-02

### Changed in 0.3.6

- Removes `kwargs`

## [0.3.5] - 2024-11-26

### Changed in 0.3.5

- In SzFactoryAbstract change `create_sz_` to `create_`

## [0.3.4] - 2024-11-04

### Changed in 0.3.4

- Fix method signature

## [0.3.2] - 2024-10-29

### Changed in 0.3.2

- Update dependencies

## [0.3.1] - 2024-10-28

### Changed in 0.3.1

- Modified signatures for find_network_by_entity_id and find_network_by_record_id

## [0.3.0] - 2024-10-27

### Added in 0.3.0

- `SzAbstractFactory`
- Updated examples

## [0.2.3] - 2024-10-09

### Changed in 0.2.3

- Update dependencies
- Update gRPC stubs

## [0.2.2] - 2024-10-04

### Added in 0.2.2

- Added `sz_engine.preprocess_record()`

### Changed in 0.2.2

- Update dependencies

## [0.2.1] - 2024-09-27

### Changed in 0.2.1

- Update dependencies
- Add `help()`

## [0.2.0] - 2024-09-25

### Added in 0.2.0

- Added `szabstractfactory`

### Changed in 0.2.0

- Update to `template-python`
- Update dependencies
- Update to latest gRPC Proto definitions

## [0.1.3] - 2024-07-29

-

### Changed in 0.1.3

- Update method signatures

## [0.1.2] - 2024-05-09

### Changed in 0.1.2

- Migrate from `g2` to `sz`
- Drop `Grpc` suffix from class names

## [0.1.1] - 2024-01-11

### Changed in 0.1.1

- Implemented g2_engine
- Added test cases

## [0.1.0] - 2024-01-05

### Changed in 0.1.0

- Renamed module to `github.com/senzing-garage/g2-sdk-python-grpc`
- Refactor to [template-python](https://github.com/senzing-garage/template-python)
- Update dependencies
  - senzing-abstract==0.0.4

## [0.0.3] - 2023-12-18

### Added to 0.0.3

- Examples using TruthSet

### Changed in 0.0.3

- Update dependencies
  - senzing-abstract==0.0.3

## [0.0.2] - 2023-12-15

### Added to 0.0.2

- Fix dependencies

## [0.0.1] - 2023-12-15

### Added to 0.0.1

- Initial functionality

[CommonMark]: https://commonmark.org/
[Keep a Changelog]: https://keepachangelog.com/
[Semantic Versioning]: https://semver.org/
