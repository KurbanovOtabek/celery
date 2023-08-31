FROM python:3.11
RUN apt-get update -y
RUN apt-get upgrade -y

ENV PYTHONUNBUFFERED=1

WORKDIR /webapp

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY . /webapp/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]