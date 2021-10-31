FROM python:3.8.3-alpine
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk del build-deps \
    && apk add --no-cache musl-dev linux-headers g++ mariadb-dev

ENV APP_PATH=/api_password
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p ${APP_PATH}
WORKDIR ${APP_PATH}

COPY . ${APP_PATH}
#RUN mkdir -p static

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r src/cognigy/requirements.txt