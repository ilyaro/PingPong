FROM alpine:latest

MAINTAINER ilyaro

RUN yum install -y python3
WORKDIR /
RUN python3 -m pip install --upgrade pip
RUN pip install flask

RUN mkdir app
COPY ./app app

EXPOSE 8089
ENTRYPOINT [ "python3" ]

CMD [ "app/hello.py" ]
