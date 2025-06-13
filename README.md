# UnderwritingParser

A Python tool for parsing and analyzing property insurance underwriting data.

## Overview

This repository contains tools for processing property insurance data, specifically designed to work with underwriting datasets that include property details, coverage information, and risk assessment features.

## Features

- Parse CSV files containing property insurance records
- Extract key information including addresses, counties, and census block groups
- Handle large datasets with error handling and validation

## Usage

### Parse Property Data

Run the main parsing script to extract address, county, and census block group information:

```bash
python parse_csv.py
```

This will process the data file and output formatted results for each property record.

## Data Structure

The parser works with datasets containing:

- **Property Identifiers**: ATTOM ID, Policy ID, Property ID
- **Location Data**: Full address, city, state, ZIP, coordinates
- **Coverage Information**: Coverage amounts, premium data
- **Property Details**: Year built, square footage, construction type
- **Risk Factors**: Roof type, foundation, HVAC systems
- **Geographic Data**: County, FIPS codes, census block groups

## Requirements

- Python 3.x
- No external dependencies (uses standard library)

## File Structure

- `parse_csv.py` - Main parsing script
- `CLAUDE.md` - Development documentation
- `.gitignore` - Git ignore rules (excludes data files)