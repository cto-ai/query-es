############################
# Final container
############################
FROM registry.cto.ai/official_images/python:latest

RUN pip3 install cto-ai

WORKDIR /ops

ADD . .