FROM python:3.11.0b4-bullseye as base

WORKDIR /app

EXPOSE 5000

RUN apt-get update && apt-get install -y sqlite3

COPY requirements.txt /app
RUN pip3 install Flask-Migrate
RUN pip3 install -r requirements.txt

COPY . /app

ENV FLASK_ENV=develop

CMD ["python3", "-m", "app", "run", "--host=0.0.0.0", "--port=5000"]