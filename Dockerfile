FROM python:3.8-slim

WORKDIR /usr/src/app
COPY *.py requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 5000

ENV FLASK_APP=tmf_simulator_app.py
CMD ["flask", "run", "--host", "0.0.0.0"]

