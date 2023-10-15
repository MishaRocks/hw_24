FROM python:3.11

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r /app/requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver"]
