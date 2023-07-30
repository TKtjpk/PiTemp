FROM python:3.9.2
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY temp_mon.py .

CMD python temp_mon.py