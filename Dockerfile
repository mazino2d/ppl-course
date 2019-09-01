FROM ubuntu:latest

MAINTAINER MAZINO

RUN apt-get update

RUN apt-get install -y  \
    python3 python3-pip \
    openjdk-8-jdk       \
    vim wget htop git

RUN pip3 install antlr4-python3-runtime

ADD https://www.antlr.org/download/antlr-4.7.2-complete.jar /lib/

COPY . /root/ppl-course/

WORKDIR /root/ppl-course/

ENV JAVA_HOME '/usr/lib/jvm/java-8-openjdk-amd64'
ENV ANTLR_JAR '/lib/antlr-4.7.2-complete.jar'

