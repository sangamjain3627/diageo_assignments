import requests
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)


def weather_data_to_csv():

    base_url = "https://community-open-weather-map.p.rapidapi.com/find"
    header = {"X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
              "X-RapidAPI-Key": "8eed59ad4amshb19701492d67fefp1d23aajsn91dd4cea7743"
              }

    states_list = ["Maharashtra,IN", "Rajasthan,IN", "Punjab,IN", "Kerala,IN", "Bihar,IN",
                   "Haryana,IN", "Gujarat,IN", "Andhra Pradesh,IN", "Uttar Pradesh,IN", "West Bengal,IN"]

    final_list = []
    for state in states_list:
        try:
            response = requests.get(base_url, params={"q": state, "units": "metric"}, 
                                    headers=header)
            if response.ok:
                curr_list = []
                data = response.json()
                curr_list.append(data['list'][0]['name'])
                curr_list.append(data['list'][0]['weather'][0]['description'])
                curr_list.append(data['list'][0]['main']['temp'])
                curr_list.append(data['list'][0]['main']['feels_like'])
                curr_list.append(data['list'][0]['main']['temp_min'])
                curr_list.append(data['list'][0]['main']['temp_max'])
                curr_list.append(data['list'][0]['main']['humidity'])
                curr_list.append(data['list'][0]['clouds']['all'])
                final_list.append(curr_list)
            else:
                logging.info(f"Invalid status code: {response.status_code}")
                logging.info(f"Message: {response.text}")
        except Exception as e:
            logging.info(f"Exception occurred while calling API: {e}")
            raise e

    logging.info("Writing api data into dataframe ...")
    df = pd.DataFrame(final_list, columns=['State', 'Description', 'Temperature', 'Feels_Like_Temperature',
                                           'Min_Temperature', 'Max_Temperature', 'Humidity', 'Clouds'])
    logging.info(f"Shape of dataframe: {df.shape}")

    # remove special chars in data received from api
    special_char = {'ā': 'a'}
    df.replace(to_replace=special_char, regex=True, inplace=True)

    logging.info(f"Creating csv file from dataframe ...")
    df.to_csv(r'~/store_files_airflow/states_weather_data.csv', index=False, header=True)
    logging.info(f"File created at location: $AIRFLOW_HOME/store_files_airflow")