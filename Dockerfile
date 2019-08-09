FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
CMD gunicorn --bind 0.0.0.0:$PORT netguru.wsgi
