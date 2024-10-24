FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /app

WORKDIR /app/drf

#EXPOSE 8000

#CMD ["python","manage.py","runserver","0.0.0.0:8000"]

