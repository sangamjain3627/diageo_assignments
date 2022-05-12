import pandas as pd
import requests
import logging

logging.basicConfig(level=logging.INFO)


def get_countries_data():
    base_url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/europe"
    header = {"X-RapidAPI-Host": "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
              "X-RapidAPI-Key": "8eed59ad4amshb19701492d67fefp1d23aajsn91dd4cea7743"}

    response_data = []
    logging.info("Requesting Covid API...")
    try:
        response = requests.get(base_url, headers=header)
        if response.ok:
            logging.info(f"API response status code: {response.status_code}")
            response_data = response.json()
        else:
            logging.info(f"Invalid status code: {response.status_code}")
    except Exception as e:
        logging.info(f"Exception occurred while calling API: {e.__traceback__}")
        raise e

    final_df = pd.DataFrame()
    for i in range(20):
        country_data = response_data[i]
        temp_df = pd.DataFrame(data=[country_data])
        final_df = pd.concat([final_df, temp_df], ignore_index=True)

    return final_df
