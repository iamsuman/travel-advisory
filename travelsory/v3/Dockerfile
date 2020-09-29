FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r travel/requirements.txt

EXPOSE 5000
WORKDIR /app/travel
CMD ["python", "/app/travel/flask_api.py"]
