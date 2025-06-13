# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains underwriting/insurance data analysis resources, specifically focused on property insurance data parsing and analysis.

## Data Structure

The main data file `_TAM_Midas_Base_Data_Set.csv` contains property insurance records with the following key information:
- Property details (address, property type, construction details)
- Insurance coverage information (policy IDs, coverage amounts, premiums)
- Property characteristics (year built, square footage, roof type, etc.)
- Geographic data (county, latitude/longitude, census data)
- Risk assessment features (foundation type, HVAC, security features)

## Data Schema

Key fields include:
- `attom_id`, `policy_id`, `property_id` - Identifiers
- Property location: `full_address`, `city`, `state`, `zip`, `latitude`, `longitude`
- Coverage: `kin_coverage_a`, `estimated_coverage_a`, `premium_surplus_fees_amount`
- Property characteristics: `attom_year_built`, `attom_sq_ft`, `property_use_standardized`
- Risk factors: `attom_roof_type`, `attom_foundation_mapped`, `attom_construction_type_mapped`

This appears to be a dataset for underwriting model development and property risk assessment.