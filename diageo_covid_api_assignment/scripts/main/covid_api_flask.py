import pandas as pd
import json

from flask import Flask
from pandasql import sqldf

app = Flask(__name__)

covid_df = pd.read_csv(r"/Users/shoaib/Desktop/covid-19_countries_entire_data.csv")
# Dataframe for affected countries
country_df = covid_df[["Country"]].copy()
country_df["DeathRate"] = round((covid_df.TotalDeaths / covid_df.TotalCases)*100, 3)
country_df["RecoveryRate"] = round((covid_df.TotalRecovered / covid_df.TotalCases)*100, 3)


@app.route("/")
def home():
    return """
    <h2>Covid-19 Data Home Page</h2>
    <h3>Visit below links to get country specific covid information</h3>
    <p style= "font-size: 15px">All countries covid information</p>
    <a href='http://127.0.0.1:5000/countries-covid-data/'>http://127.0.0.1:5000/countries-covid-data/</a> 
    <p style= "font-size: 15px">Most affected country (Country with highest Death rate)</p>
    <a href='http://127.0.0.1:5000/countries-covid-data/most-affected-country/'>http://127.0.0.1:5000/countries-covid-data/most-affected-country/</a>
    <p style= "font-size: 15px">Least affected country (Country with lowest Death rate)</p>
    <a href='http://127.0.0.1:5000/countries-covid-data/least-affected-country/'>http://127.0.0.1:5000/countries-covid-data/least-affected-country/</a>
    <p style= "font-size: 15px">Country recording highest number of covid cases</p>
    <a href='http://127.0.0.1:5000/countries-covid-data/country-with-highest-cases/'>http://127.0.0.1:5000/countries-covid-data/country-with-highest-cases/</a>
    <p style= "font-size: 15px">Country recording minimum number of covid cases</p>
    <a href='http://127.0.0.1:5000/countries-covid-data/country-with-minimum-cases/'>http://127.0.0.1:5000/countries-covid-data/country-with-minimum-cases/</a>
    <p style= "font-size: 15px">Total covid cases recorded by all countries combined</p>
    <a href='http://127.0.0.1:5000/countries-covid-data/total-covid-cases/'>http://127.0.0.1:5000/countries-covid-data/total-covid-cases/</a>
    <p style= "font-size: 15px">Country with highest recovery against covid</p>
    <a href='http://127.0.0.1:5000/countries-covid-data/country-with-highest-recovery/'>http://127.0.0.1:5000/countries-covid-data/country-with-highest-recovery/</a>
    <p style= "font-size: 15px">Country with minimum recovery against covid</p>
    <a href='http://127.0.0.1:5000/countries-covid-data/country-with-minimum-recovery/'>http://127.0.0.1:5000/countries-covid-data/country-with-minimum-recovery/</a>
    <p style= "font-size: 15px">Country least suffering from covid</p>
    <a href='http://127.0.0.1:5000/countries-covid-data/country-least-suffering-from-covid/'>http://127.0.0.1:5000/countries-covid-data/country-least-suffering-from-covid/</a>
    <p style= "font-size: 15px">Country still suffering from covid</p>
    <a href='http://127.0.0.1:5000/countries-covid-data/country-still-suffering-from-covid/'>http://127.0.0.1:5000/countries-covid-data/country-still-suffering-from-covid/</a>
     """


@app.route("/countries-covid-data/")
def countries_data():
    parsed = json.loads(covid_df.to_json(orient='records'))
    response = app.response_class(
        response=json.dumps(parsed, indent=2),
        status=200,
        mimetype="application/json"
    )
    return response


@app.route("/countries-covid-data/most-affected-country/")
def most_affected_country():
    output = sqldf("""SELECT Country, DeathRate FROM country_df 
                    ORDER BY DeathRate DESC 
                    LIMIT 1""")
    parsed = json.loads(output.to_json(orient='records'))
    response = app.response_class(
        response=json.dumps(parsed, indent=2),
        status=200,
        mimetype="application/json"
    )
    return response


@app.route("/countries-covid-data/least-affected-country/")
def least_affected_country():
    output = sqldf("""SELECT Country, DeathRate FROM country_df 
                    ORDER BY DeathRate 
                    LIMIT 1""")
    parsed = json.loads(output.to_json(orient='records'))
    response = app.response_class(
        response=json.dumps(parsed, indent=2),
        status=200,
        mimetype="application/json"
    )
    return response


@app.route("/countries-covid-data/country-with-highest-cases/")
def highest_cases():
    output = sqldf("""SELECT Country, TotalCases FROM covid_df 
                    ORDER BY TotalCases DESC 
                    LIMIT 1""")
    parsed = json.loads(output.to_json(orient='records'))
    response = app.response_class(
        response=json.dumps(parsed, indent=2),
        status=200,
        mimetype="application/json"
    )
    return response


@app.route("/countries-covid-data/country-with-minimum-cases/")
def minimum_cases():
    output = sqldf("""SELECT Country, TotalCases FROM covid_df 
                    ORDER BY TotalCases 
                    LIMIT 1""")
    parsed = json.loads(output.to_json(orient='records'))
    response = app.response_class(
        response=json.dumps(parsed, indent=2),
        status=200,
        mimetype="application/json"
    )
    return response


@app.route("/countries-covid-data/total-covid-cases/")
def total_cases():
    output = sqldf("""SELECT sum(TotalCases) AS TotalCovidCases FROM covid_df""")
    parsed = json.loads(output.to_json(orient='records'))
    response = app.response_class(
        response=json.dumps(parsed, indent=2),
        status=200,
        mimetype="application/json"
    )
    return response


@app.route("/countries-covid-data/country-with-highest-recovery/")
def highest_recovery():
    output = sqldf("""SELECT Country, RecoveryRate FROM country_df 
                    ORDER BY RecoveryRate DESC
                    LIMIT 1""")
    parsed = json.loads(output.to_json(orient='records'))
    response = app.response_class(
        response=json.dumps(parsed, indent=2),
        status=200,
        mimetype="application/json"
    )
    return response


@app.route("/countries-covid-data/country-with-minimum-recovery/")
def minimum_recovery():
    output = sqldf("""SELECT Country, RecoveryRate FROM country_df 
                    ORDER BY RecoveryRate
                    LIMIT 1""")
    parsed = json.loads(output.to_json(orient='records'))
    response = app.response_class(
        response=json.dumps(parsed, indent=2),
        status=200,
        mimetype="application/json"
    )
    return response


@app.route("/countries-covid-data/country-least-suffering-from-covid/")
def least_suffering():
    output = sqldf("""SELECT Country, Serious_Critical FROM covid_df 
                    ORDER BY Serious_Critical
                    LIMIT 1""")
    parsed = json.loads(output.to_json(orient='records'))
    response = app.response_class(
        response=json.dumps(parsed, indent=2),
        status=200,
        mimetype="application/json"
    )
    return response


@app.route("/countries-covid-data/country-still-suffering-from-covid/")
def most_suffering():
    output = sqldf("""SELECT Country, Serious_Critical FROM covid_df 
                    ORDER BY Serious_Critical DESC
                    LIMIT 1""")
    parsed = json.loads(output.to_json(orient='records'))
    response = app.response_class(
        response=json.dumps(parsed, indent=2),
        status=200,
        mimetype="application/json"
    )
    return response


# Run the flask app
def run_app():
    app.run()
