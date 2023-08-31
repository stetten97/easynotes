FROM python:3.11.0b4-bullseye as base

WORKDIR /app

RUN apt-get update && apt-get install -y sqlite3

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]