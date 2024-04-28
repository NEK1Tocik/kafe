import requests
import datetime
from datetime import datetime, timedelta
from django.conf import settings


class OrderProcessor:

    def __init__(self, dag_name):
        self.dag_name = dag_name
        self.headers = None
        self.json_data = None
        self.tims = None

    def time_generator(self):
        self.tims = (
                (datetime.now() +
                 timedelta(minutes=1) -
                 timedelta(hours=3)).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] +
                'Z'
        )
        pass

    def response_data_preparer(self):
        self.headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        self.json_data = {
            'conf': {},
            'dag_run_id': self.tims,
            'logical_date': self.tims,
            'note': 'string',
        }
        pass

    def run_dag(self):
        self.time_generator()
        self.response_data_preparer()
        requests.post(f'http://127.0.0.1:8080/api/v1/dags/{self.dag_name}/dagRuns',
                      headers=self.headers,
                      json=self.json_data,
                      auth=('airflow', 'airflow'))


if __name__ == '__main__':
    test = OrderProcessor('pizza_dag')
    test.run_dag()
