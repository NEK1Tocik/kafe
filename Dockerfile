FROM apache/airflow:2.7.3

#WORKDIR app/
#COPY . /app
#COPY . /opt/airflow

RUN python -m pip install --upgrade pip
RUN pip install --upgrade pip
RUN pip install django
RUN pip install pytelegrambotapi


CMD ["echo", "hello"]
