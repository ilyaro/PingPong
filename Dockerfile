FROM alpine:latest

MAINTAINER ilyaro

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
WORKDIR /
RUN pip install flask

RUN mkdir app
COPY ./app app

ENTRYPOINT [ "python3" ] 

CMD  ["app/pingpong_ms.py", "8089"]
