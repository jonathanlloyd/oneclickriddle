FROM python:3.7.1-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install gunicorn

CMD gunicorn ocr_server.app:app
