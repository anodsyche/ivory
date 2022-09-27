FROM python:3.9-alpine

ADD . /app
WORKDIR /app
COPY . /app
RUN pip3 install --upgrade pip  
RUN pip3 install -r requirements.txt

CMD ["python3","run.py"]