FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app


RUN pip install --upgrade pip

COPY ./setup.cfg .
COPY ./setup.py .
COPY ./entrypoint.sh .

RUN chmod +x entrypoint.sh

RUN pip install --no-cache-dir --upgrade -e '.[dev]'

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]