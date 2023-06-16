FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app/

COPY ./my_cv_django/requirements.txt requirements.txt

RUN pip install --upgrade pip && pip3 install -r requirements.txt
