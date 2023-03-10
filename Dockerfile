# syntax=docker/dockerfile:1
FROM python:3.10-slim-buster
WORKDIR .
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "client_bot.py"]