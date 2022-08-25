# syntax=docker/dockerfile:1
FROM python:3.10.6-slim-buster
WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]