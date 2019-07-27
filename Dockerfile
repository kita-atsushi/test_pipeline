FROM python:3.6.9-alpine

COPY requirements.txt /
RUN pip install -r requirements.txt
COPY app.py /

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

CMD ["hug", "-f", "/app.py"]

