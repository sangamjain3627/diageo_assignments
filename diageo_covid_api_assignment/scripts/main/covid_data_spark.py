import json
import logging

from pyspark.sql import SparkSession
from pyspark.sql.functions import round, sum, col

logging.basicConfig(level=logging.INFO)


def create_spark_session():
    logging.info("Creating spark session....")
    spark_session = SparkSession.builder.master('local[4]').appName('PySpark Assignment Demo').getOrCreate()
    spark_session.sparkContext.setLogLevel('ERROR')
    logging.info("Spark session created successfully!")
    return spark_session


def get_covid_answers_from_spark_dataframe():
    spark = create_spark_session()
    spark_df = spark.read.csv(r'/Users/shoaib/Desktop/covid-19_countries_entire_data.csv',
                              header=True, inferSchema=True)

    logging.info(f"Schema of Spark Dataframe: ")
    spark_df.printSchema()
    country_df = spark_df.select('Country',
                                 round((spark_df.TotalDeaths / spark_df.TotalCases)*100, 3).alias('DeathRate'),
                                 round((spark_df.TotalRecovered / spark_df.TotalCases)*100, 3).alias('RecoveryRate')
                                 )
    logging.info(f"Country dataframe with DeathRate and RecoveryRate: ")
    country_df.show()

    # 2.1) Most affected country among all the countries
    print("Most affected country among all the countries")
    country_df.select('Country', 'DeathRate').orderBy(col('DeathRate').desc()).show(1)

    # 2.2) Least affected country among all the countries
    print("Least affected country among all the countries")
    country_df.select('Country', 'DeathRate').orderBy(col('DeathRate').asc()).show(1)

    # 2.3) Country with the highest covid cases
    print("Country with the highest covid cases")
    spark_df.select('Country', 'TotalCases').orderBy(col('TotalCases').desc()).show(1)

    # 2.4) Country with minimum covid cases
    print("Country with minimum covid cases")
    spark_df.select('Country', 'TotalCases').orderBy(col('TotalCases').asc()).show(1)

    # 2.5) Total Cases
    print("Total covid cases for all countries combined")
    spark_df.select(sum('TotalCases').alias('TotalCovidCases')).show()

    # 2.6) Country that handled the covid most efficiently
    print("Country that handled the covid most efficiently")
    country_df.select('Country', 'RecoveryRate').orderBy(col('RecoveryRate').desc()).show(1)

    # 2.7) Country that handled the covid least efficiently
    print("Country that handled the covid least efficiently")
    country_df.select('Country', 'RecoveryRate').orderBy(col('RecoveryRate').asc()).show(1)

    # 2.8) Country least suffering from covid
    print("Country least suffering from covid")
    spark_df.select('Country', 'Serious_Critical').orderBy(col('Serious_Critical').asc()).show(1)

    # 2.9) Country still suffering from covid
    print("Country still suffering from covid")
    spark_df.select('Country', 'Serious_Critical').orderBy(col('Serious_Critical').desc()).show(1)

