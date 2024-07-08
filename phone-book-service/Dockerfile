FROM python:3.10

WORKDIR app

COPY requirements.txt .
COPY app .

RUN pip install -r requirements.txt

CMD python app.py
