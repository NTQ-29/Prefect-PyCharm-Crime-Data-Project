# Prefect-PyCharm-Crime-Data-Project
Downloaded Prefect, the open Python orchestration tool, to run an imported json file from data.lacity.org about Crime Data from 2020 to 2024. This is in progress of facilitating an End-to_End Pipeline from Python to Prefect Dashboard.

# LA Crime Data Pipeline (In Progress)

> A data engineering pipeline built with Prefect and Python
> that fetches, cleans, and summarizes publicly available
> crime data from the City of Los Angeles open data API.

## Overview

This project demonstrates a basic ETL (Extract, Transform, Load)
pipeline using Prefect as the orchestration framework. It is
currently a work in progress, with the goal of expanding into
a full pipeline with persistent storage and scheduled runs.

## Pipeline stages

- **Extract** — fetches records from the LA City open data API
- **Transform** — normalizes field names and cleans raw records
- **Summarize** — logs record counts and pipeline completion status

## Tech stack

- Python 3.10+
- [Prefect](https://www.prefect.io/) — workflow orchestration
- [httpx](https://www.python-httpx.org/) — HTTP requests
- [LA Crime Data API](https://data.lacity.org/resource/2nrs-mtv8.json) — public data source

## Getting started

### Prerequisites

- Python 3.10+
- A free [Prefect Cloud](https://app.prefect.cloud/) account

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/la-crime-pipeline.git
cd la-crime-pipeline
pip install -r requirements.txt
```

### Authenticate with Prefect Cloud

```bash
prefect cloud login
```

### Run the pipeline

```bash
python main.py
```

The flow will register as a deployment named
`crime-data-deployment-collector` and begin serving.

## Project structure

```
la-crime-pipeline/
├── main.py            # pipeline entry point
├── requirements.txt   # dependencies
└── README.md
```

## Roadmap

- [ ] Add a load stage to persist cleaned records to a database
- [ ] Add scheduling (run nightly or hourly)
- [ ] Add error handling and retry logic on failed API calls
- [ ] Expand fields captured in the transform stage
- [ ] Add unit tests

## Status

**In progress.** Core extract and transform stages are functional.
Load stage and scheduling are not yet implemented.

## Data source

[Los Angeles Open Data — Crime Data from 2020 to Present](https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8)
Licensed under the City of Los Angeles open data terms.
