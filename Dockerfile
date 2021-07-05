FROM python:alpine

WORKDIR /app

COPY ./src /app

RUN pip install Flask

CMD ["python", "main.py"]
