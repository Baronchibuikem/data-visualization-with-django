# pull official base image
FROM python:3.8.3-alpine


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#for m1 mac users who will have issue with cryptography library
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1    

# # install psycopg2 dependencies
# RUN apk update
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN chmod +x /entrypoint.sh
