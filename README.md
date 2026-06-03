# AgriPride Multi-Agent Lending Pride Core (Option B)

This repository contains the live prototype of the AgriPride autonomous multi-agent ecosystem designed for SASRA regulatory compliance.

## System Architecture
- **Scout Agent (RANK Calibrated):** Handles initial data ingestion and yield tracking.
- **Guardian Agent (RANK & TRAIL Bounded):** Controls credit risk triage up to KES 25,000.
- **HUNT Protocol:** Automated handoff executes when `Verified Harvest Mass >= 500kg`.
- **Data Sovereignty:** Hardcoded storage targets restricted exclusively to the AWS Africa (Cape Town) cloud region per the Kenya Data Protection Act 2022.

## Setup & Execution
1. Install requirements: `pip install crewai`
2. Configure your local sovereign environment variables.
3. Run the ecosystem validation check: `python agri_pride_core.py`
