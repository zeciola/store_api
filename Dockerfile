FROM python:3.7.6-alpine

WORKDIR /usr/src/store_api

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY . .

ENTRYPOINT ./run.sh
