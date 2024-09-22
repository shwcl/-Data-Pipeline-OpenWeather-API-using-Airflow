
from airflow import DAG
from datetime import timedelta, datetime
from airflow.providers.http.sensors.http import HttpSensor
import json
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
import pandas as pd


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 21),
    'email':['myemail@domain.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}


def kelvin_to_celsius(temp_in_kelvin):
    celsius = temp_in_kelvin - 273.15
    return celsius


def transform_load_weather_data(task_instance):

    # extract data
    data = task_instance.xcom_pull(task_ids="extract_weather_data")
    weather_description = data["weather"][0]["description"]
    temp_celsius = kelvin_to_celsius(data["main"]["temp"])
    temp_feels_like_celsius = kelvin_to_celsius(data["main"]["feels_like"])
    temp_min_celsius = kelvin_to_celsius(data["main"]["temp_min"])
    temp_max_celsius = kelvin_to_celsius(data["main"]["temp_max"])
    atmospheric_pressure = data["main"]["pressure"]
    humidity = data['main']['humidity']
    visibility = data["visibility"]
    wind_speed = data['wind']["speed"]
    wind_direction = data["wind"]["deg"]
    cloudiness = data["clouds"]["all"]
    time_of_record = datetime.utcfromtimestamp(data["dt"]+ data['timezone'])
    sunrise = datetime.utcfromtimestamp(data["sys"]["sunrise"] + data['timezone'])
    sunset = datetime.utcfromtimestamp(data["sys"]["sunset"] + data['timezone'])
    country = data["sys"]["country"]
    city = data["name"]



    transformed_data = {
        "weather_description": weather_description,
        "temp_celsius": temp_celsius,
        "temp_feels_like_celsius": temp_feels_like_celsius,
        "temp_min_celsius": temp_min_celsius,
        "temp_max_celsius": temp_max_celsius,
        "atmospheric_pressure": atmospheric_pressure,
        "humidity": humidity,
        "visibility": visibility,
        "wind_speed": wind_speed,
        "wind_direction": wind_direction,
        "cloudiness": cloudiness,
        "time_of_record": time_of_record,
        "sunrise": sunrise,
        "sunset": sunset,
        "country": country,
        "city": city
    }


    transform_load_data_list = [transformed_data]

    df = pd.DataFrame(transform_load_data_list)

    # output to csv and load to s3
    aws_credentials = {
        "key": "A...........",
        "secret": ".......................",
        "token": "..............."
    }

    current_time = datetime.now()
    dt_format = current_time.strftime('%Y%m%d%H%M%S')
    df.to_csv('s3://current-weather-data-store01/weather_data_{}.csv'.format(dt_format), index=False, storage_options=aws_credentials)


with DAG('gy_weather_data_dag',
    default_args = default_args,
    schedule_interval = '@daily',
    catchup = False) as dag:


    is_open_weather_api_ready = HttpSensor(
    task_id = 'is_open_weather_api_ready',
    http_conn_id = 'open_weather_api',
    endpoint = '/data/2.5/weather?q=georgetown,gy&appid=...................'
    )

    extract_weather_data = SimpleHttpOperator(
    task_id = 'extract_weather_data',
    http_conn_id = 'open_weather_api',
    endpoint = '/data/2.5/weather?q=georgetown,gy&appid=.................',
    method = 'GET',
    response_filter = lambda response : json.loads(response.text),
    log_response = True
    )


    transform_load_weather_data = PythonOperator(
    task_id = 'transform_load_weather_data',
    python_callable = transform_load_weather_data
    )

    is_open_weather_api_ready >> extract_weather_data >> transform_load_weather_data

