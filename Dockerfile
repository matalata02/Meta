FROM debian:latest
FROM python:3.10.2-bullseye
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y 
RUN pip3 install -U pip
RUN curl -sL https://deb.nodesource.com/setup_18.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir --upgrade --requirement https://raw.githubusercontent.com/gsweq11/codeword/main/requirements.txt
CMD [ "bash", "start" ]
