FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt  ./ 
RUN pip3 install --requirement requirements.txt

COPY setup.py ./
COPY logmia logmia/
RUN pip3 install .

CMD [ "pytest"]
