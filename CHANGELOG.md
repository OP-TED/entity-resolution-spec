# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]
### Added

### Changed
* data model changed according to recent
  * Terminology cleaned (eg, "cluster reference" in place of "alignment option")
	* Simplifications (eg, alignment set removed)
	* Entity mention ID based on `requestID` + `sourceID` + `entityType`
* Documentation updates, eg, sequence diagram
* Gherkin tests updated according to the cases described in the new ERE Technical Contract


## [0.1.0-rc.2] - 2026-01-16
### Added
* data model: Support for rejected canonical identifiers
* data model: Support for a full rebuild

### Changed
* Updated and refined data model
* Updated ERS-ERE  examples


## [0.1.0-rc.1] - 2025-12-22

* Initial release, fulfilling Project's Delivery 1 (ERE Technical Contract and related code).
* [LinkML schema](resources/schema/ers-core_v0.1.0.yaml) to specify the interaction with the ERE service.
	* Includes auto-generated [navigable documents](docs/schema/README.md), a [class diagram](docs/schema/README.md) and a [sequence diagram](docs/ere-interface-seq-diag.png).
* [Gherkin Tests](test/features/), based on [collected test data](test/test_data/), possible [test cases](test/test_data/analysis/README.md)

