# Dockerfile para el backend de Hermes GO
FROM python:3.8-alpine
# esto permite que los mensajes de salida se envíen inmediatamente a la consola
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /django

# Actualizar pip
# RUN /usr/local/bin/python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt
