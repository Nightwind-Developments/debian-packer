# Sets the OS Image to use
FROM ubuntu:20.04

# Installs Pre-Requisites
RUN apt-get update && apt-get install -y python3 python3-pip

# Copies Code Files
COPY debianpacker.py /
COPY setup.py /
