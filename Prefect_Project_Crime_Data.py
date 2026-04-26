import httpx
#imports asynchronous & synchronous http requests | quick & reliable APIs
from prefect import flow, get_run_logger, task
#get_run_logger = Prefect helper function | orchestration framework workflow
#log messages are captured and managed in Prefect logging system
#task = smallest unit in Prefect Workflow | decorate like @flow and it's @task
#callable like a Python function ( ) & allows you to scale horizontally & vertically
BASE_URL = "https://data.lacity.org/resource/2nrs-mtv8.json"
#open JSON API (auth not required)
@task
def get_from_api() -> list[dict]:
    my_logger = get_run_logger()
    response = httpx.get(BASE_URL)
    response = httpx.get(BASE_URL, params={"limit": 50}) #gives limits to the data
    response.raise_for_status()
    crime_data = response.json()
    my_logger.info(f"Fetched {len(crime_data)} records")
    return crime_data
    #for downstream tasks, the crime_data needs to be returned
@task
def clean_crime_data(crime_records: list[dict]) -> list[dict]:
    # place argument from crime to set up clean data Prefect task
    cleaned = []
    for crime in crime_records:
        cleaned.append({
            "crm_cd": crime.get("crm_cd") or crime.get("Crm_Cd", "unknown"),
            "date_occ": crime.get("date_occ", ""),
            "area_name": crime.get("area_name", ""),
        })
    return cleaned
  # makes sure there's no case-sensitive errors for crime committed
@task
def summarize (cleaned_records: list[dict]):
    my_logger = get_run_logger()
    my_logger.info(f"Pipeline complete. {len(cleaned_records)} cleaned records ready.")
    #setting up the logger to get real-time metrics from agent w/ f-strings

#importing the flow decorator from Prefect Package | for showing orchestration workflows
@flow #since we're using Prefect, we'll need to use @Flow to signify it
#defining the self-directed function (SDF) for crime data
def crime_data():
   crime = get_from_api()
   cleaned = clean_crime_data(crime) #wires tasks together
   summarize(cleaned)
   #summarization of the cleaned data

def main():
    crime_data.serve("crime-data-deployment-collector")
    #acts as an agent to retrieve ingress for the flow

if __name__ == "__main__":
    main()
    #makes code reusable and keeps entry point to code clear