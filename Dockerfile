FROM python:3.7

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENV FLASK_APP /app/app.py

EXPOSE 5000
CMD ["flask","run","--host=0.0.0.0"]