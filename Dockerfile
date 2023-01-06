FROM python:3.8-slim-buster

RUN apt-get -y update
RUN apt-get -y upgrade

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN poetry install

EXPOSE 8080

CMD ["poetry", "run", "server"]