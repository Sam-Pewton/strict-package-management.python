FROM python:3.7-alpine
WORKDIR /app
ADD requirements.txt /app
RUN PYTHONPATH=/usr/bin/python pip install -r /app/requirements.txt
COPY . /app
CMD [ "pytest" ]
