from diageo_covid_api_assignment.scripts.main.covid_data_web import get_countries_data
from diageo_covid_api_assignment.scripts.main.covid_data_spark import get_covid_answers_from_spark_dataframe
from diageo_covid_api_assignment.scripts.main.covid_api_flask import run_app

if __name__ == '__main__':
    covid_web_data = get_countries_data()
    # Save to a local csv file
    covid_web_data.to_csv(r'/Users/shoaib/Desktop/covid-19_countries_entire_data.csv', index=False, header=True)
    get_covid_answers_from_spark_dataframe()
    run_app()
