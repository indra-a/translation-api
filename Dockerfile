FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 8000

WORKDIR /code/app

CMD uvicorn main:app --host 0.0.0.0 --port 8000