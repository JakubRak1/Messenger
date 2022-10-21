FROM python:3

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 120

CMD ["python", "./run.py"]