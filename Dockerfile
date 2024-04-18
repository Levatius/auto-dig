FROM python:3.11-bullseye

RUN pip install -r requirements.txt

RUN ["python", "app.py"]