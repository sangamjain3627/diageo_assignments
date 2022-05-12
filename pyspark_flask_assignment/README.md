## This project is about Pyspark and Flask assignment for Diageo training.

> Before starting, download the required packages from **requirements.txt** file


#### Note: Path to store the csv file is used as local Desktop path, replace it with your local path

This project aims to build understanding and working knowledge of **Pyspark** and **Flask** framework by making use of Covid web API and answering required questions.
2) Using Spark dataframe, find out the following:
2.1) Most affected country among all the countries ( total death/total covid cases).
2.2) Least affected country among all the countries ( total death/total covid cases).
2.3) Country with highest covid cases.
2.4) Country with minimum covid cases.
2.5) Total cases.
2.6) Country that handled the covid most efficiently( total recovery/ total covid cases).
2.7) Country that handled the covid least efficiently( total recovery/ total covid cases).
2.8) Country least suffering from covid ( least critical cases).
2.9) Country still suffering from covid (highest critical cases).
3) Create a RestFul API to show datas collected in question 1.
4) Create each RestFul API to show result of every sub question in question 2.

For questions 3 & 4 we used Flask framework to build RESTFul APIs on **localhost** (http://127.0.0.1:5000/) with default **port-5000**.
The API Endpoints are given below,
> /countries-covid-data/  (Answer to main question 3)
> /countries-covid-data/most-affected-country/  (Answer to subquestion 2.1)
> /countries-covid-data/least-affected-country/ (Answer to subquestion 2.2)
> /countries-covid-data/country-with-highest-cases/ (Answer to subquestion 2.3)
> /countries-covid-data/country-with-minimum-cases/ (Answer to subquestion 2.4)
> /countries-covid-data/total-covid-cases/          (Answer to subquestion 2.5)
> /countries-covid-data/country-with-highest-recovery/  (Answer to subquestion 2.6)
> /countries-covid-data/country-with-minimum-recovery/  (Answer to subquestion 2.7)
> /countries-covid-data/country-least-suffering-from-covid/ (Answer to subquestion 2.8)
> /countries-covid-data/country-still-suffering-from-covid/ (Answer to subquestion 2.9)
