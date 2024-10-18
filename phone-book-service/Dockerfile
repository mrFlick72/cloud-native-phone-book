FROM python:3.10

COPY requirements.txt .
COPY src .

RUN pip install -r requirements.txt

CMD python app.py