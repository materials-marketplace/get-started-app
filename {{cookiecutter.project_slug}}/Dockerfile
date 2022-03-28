FROM python:3.8

RUN apt-get update && apt-get install -y curl
RUN pip install --upgrade pip
RUN pip install flask requests-oauthlib

WORKDIR /app
ADD app.py .
ADD static .


ENV FLASK_APP=app.py

ENV PORT=5000

CMD flask run --host=0.0.0.0 --port=${PORT}
