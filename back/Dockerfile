FROM python:3
RUN apt-get update

# name of the container
LABEL maintainer="backend-hermes-GO"

# Actualizar pip
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install Django==4.1.6
COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir

# trasladar archivos 
COPY core ./core

# RUN cd core
RUN python3 core/manage.py makemigrations
RUN python3 core/manage.py migrate
# RUN python3 core/manage.py runserver


EXPOSE 7070
# python run server
ENTRYPOINT ["python3"] 
CMD ["core/manage.py", "runserver", "0.0.0.0:7070"]
