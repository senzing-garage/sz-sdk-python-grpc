# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog], [markdownlint],
and this project adheres to [Semantic Versioning].

## [Unreleased]

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
- UKpdataed examples

## [0.2.3] - 2024-10-09

### Changed in 0.2.3

- Update dependencies
- Update gRPC stubs

## [0.2.2] - 2024-10-04

### Added in 0.2.2

- Added `sz_enzine.preprocess_record()`

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

[Keep a Changelog]: https://keepachangelog.com/en/1.0.0/
[markdownlint]: https://dlaa.me/markdownlint/
[Semantic Versioning]: https://semver.org/spec/v2.0.0.html
