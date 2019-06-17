FROM python:3.7-alpine

COPY /app /app
COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENV client_id="id"
ENV client_secret="secret"
ENV pg_num=1
ENV message_content="Hello World"

CMD  python bulk-tool.py $ENV1 $ENV2 $ENV3 $ENV4