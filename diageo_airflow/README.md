## This project is about implementing Airflow Dag for Diageo training.



**To get started, install Docker Desktop on your pc**

This project aims to build understanding and working knowledge of **Airflow** by creating a dag **weather_dag** and loading weather data into a table using **postgres** database

Download this github project's zip file and extract this file on your PC.  
Navigate to this extracted folder path in your terminal window and run the follwing docker command:
> docker-compose -f docker-compose-weather.yml up -d

This will run the **.yml** file and pull required images and mount required directory path in the container created for the images.
> docker ps

Run the above command in terminal to check the running containers
You should see **postgres** and **airflow** containers up and running

To run the dag go to web address **localhost** (http://127.0.0.1:8080/) with **port-8080** being default port for airflow webserver.  
Trigger the dag and wait for its completion.  
Once completed, run:  
> docker ps

and grab the Container Id of postgres container and run below command to enter into container's bash mode
> docker exec -it <container_id> bash

Now get the postgres **username** from **docker-compose-weather.yml** file and use it to start using postgres database by running:
> psql -U <user_name>

Connect to the database that is specified in **docker-compose-weather.yml** file using command:
> \c <database_name>

Now once connected to database, run select query to confirm data is loaded into **weather** table
> SELECT * FROM weather;

To exit from container press **Ctrl+D**

