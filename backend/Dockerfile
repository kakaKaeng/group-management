FROM python:3.8

ENV PYTHONUNBUFFERED 1

# Location of source code
ENV PROJECT_ROOT /opt/app
RUN mkdir -p $PROJECT_ROOT
WORKDIR $PROJECT_ROOT

COPY ./manage.py .

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY management ./management
