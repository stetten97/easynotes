FROM python:3.11.0b4-bullseye as base

WORKDIR /easynotes

EXPOSE 5000

RUN apt-get update && apt-get install -y sqlite3

COPY requirements.txt /easynotes
RUN pip3 install Flask-Migrate
RUN pip3 install -r requirements.txt

COPY . /easynotes/

ENV FLASK_ENV=develop
ENV FLASK_DEBUG=True
ENV FLASK_APP=__init__.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]