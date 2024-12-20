import logging
import os
import uuid
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Configurar logging
log_directory = "C:/Users/Desktop/airflow/logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)
log_file = os.path.join(log_directory, 'user_automation.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

default_args = {
    'owner': 'jaquesson',
    'start_date': datetime(2024, 11, 20, 10, 0)
}


def get_data():
    import requests

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]

    return res


def format_data(res):
    data = {}
    location = res['location']
    data['id'] = uuid.uuid4()
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data


def stream_data():
    import json
    from kafka import KafkaProducer
    import time

    producer = KafkaProducer(
        bootstrap_servers=['broker:29092'], max_block_ms=5000)
    curr_time = time.time()

    while True:
        if time.time() > curr_time + 60:  # 1 minute
            break
        try:
            res = get_data()
            res = format_data(res)

            producer.send('users_created', json.dumps(res).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occurred: {e}')
            continue


with DAG('user_automation',
         default_args=default_args,
         schedule=timedelta(days=1),
         catchup=False) as dag:

    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )
