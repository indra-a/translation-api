# FastAPI-Mongolian-English-Translation

This repository contains a FastAPI application for translating between Mongolian and English languages. The application is dockerized for easy deployment and scalability.

## Model

This application utilizes Meta's No Language Left Behind (NLLB) model (https://ai.meta.com/research/no-language-left-behind/) for performing translation between Mongolian and English languages. The NLLB model is a state-of-the-art neural machine translation model designed to support a wide range of languages, including low-resource languages like Mongolian.


## Features

- Translate text from Mongolian to English
- Translate text from English to Mongolian
- Dockerized application for easy deployment

## Prerequisites

Before running the application, ensure that you have the following installed:

- Docker
- Docker Compose (if using the provided Docker Compose file)

## Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/fastapi-mongolian-english-translation.git
cd fastapi-mongolian-english-translation
```

2. Docker Compose

```bash
docker-compose up
```

## API Endpoints

Once the application is running, you can access the following endpoints:

- `/translate/mongolian-to-english (POST):` Translate text from Mongolian to English
- `/translate/english-to-mongolian (POST):` Translate text from English to Mongolian

Both endpoints accept a JSON payload with a text field containing the text to be translated.

Example request:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "Сайн байна уу"}' http://localhost:8000/translate/mongolian-to-english
```

## Further works

In the future, I'm planning to improve the performance by finetuning this model on custom dataset.
Enjoy!