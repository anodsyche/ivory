FROM python:3.9-alpine

ENV REDIS_OM_URL=redis://redis:6379

RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev

ADD . /app
WORKDIR /app
COPY . /app
RUN pip3 install --upgrade pip  
RUN pip3 install -r requirements.txt

CMD ["python3","run.py"]