FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements-prod.txt /code/
RUN pip install -r requirements-prod.txt
COPY . /code/