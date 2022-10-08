# 
FROM python:3.8 as requirements-stage

WORKDIR /app/

COPY ./main.py /app/
COPY ./requirements.txt /app/

RUN pip install -r requirements.txt
RUN pip install python-dotenv
RUN pip install --upgrade 'sentry-sdk[fastapi]'

CMD uvicorn --host=0.0.0.0 --port 8000 main:app