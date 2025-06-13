# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains Python tools for parsing and analyzing property insurance underwriting data. The main focus is on processing CSV datasets containing property details, coverage information, and risk assessment features for underwriting model development.

## Commands

### Running the Parser
```bash
python parse_csv.py
```
Parses the CSV data file and outputs address, county, and census block group information for each property record.

## Project Structure

- `parse_csv.py` - Main CSV parsing script using Python's csv.DictReader
- `_TAM_Midas_Base_Data_Set.csv` - Source data file (excluded from git via .gitignore)
- `README.md` - Project documentation
- `LICENSE` - MIT license

## Data Schema

The CSV contains property insurance records with these key fields:
- **Identifiers**: `attom_id`, `policy_id`, `property_id`
- **Location**: `full_address`, `city`, `state`, `zip`, `latitude`, `longitude`, `county`
- **Coverage**: `estimated_coverage_a`, `premium_surplus_fees_amount`
- **Property Info**: `attom_year_built`, `attom_sq_ft`, `property_use_standardized`
- **Risk Factors**: `attom_roof_type`, `attom_foundation_mapped`, `attom_construction_type_mapped`
- **Geographic**: `county_fips`, `attom_census_block_group`

## Development Notes

- CSV files are excluded from version control via .gitignore
- Script includes error handling for missing files and malformed data
- Uses standard library only (no external dependencies required)