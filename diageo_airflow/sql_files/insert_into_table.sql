TRUNCATE TABLE weather;
COPY weather FROM '/store_files_psql/states_weather_data.csv' DELIMITER ',' CSV HEADER;