FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /

EXPOSE 8000

ADD . /

RUN pip install -r requirements.txt


CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]