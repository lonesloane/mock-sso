FROM python:3.6-alpine

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8086

CMD ["python", "app.py"]