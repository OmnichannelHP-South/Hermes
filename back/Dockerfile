# Dockerfile para el backend de Hermes GO
FROM python:3.8.5-slim-buster

# esto permite que los mensajes de salida se envíen inmediatamente a la consola
ENV PYTHONUNBUFFERED=1
WORKDIR /backend

# Actualizar pip
RUN /usr/local/bin/python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
