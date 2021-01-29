# airmeet_test

## Pre-requisites

Docker

## Descrption

I have used flask as my web framework & addded the api in app.py

I have used python3.7 in my dockerfile and the image is exposed at port 5000.

You can build docker image using below command with tag v1
```bash
docker build -t airmeet-metrics:v1 .
```
Once image is built, you can run below command to start a container with port 8080 oon your local.
```bash
docker run -d -p 8080:5000 airmeet-metrics:v1
```
## Extras
In this, We use list to handle the metric collection.

Flask-Cache's simple cache strategy is not thread safe. You will need to use an external server one way or another it seems. 
If it demands the scale, then we can move to using redis .