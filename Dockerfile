FROM debian:latest

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
RUN curl -sL https://deb.nodesource.com/setup_15.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
WORKDIR /app/
COPY . /app/
RUN pip3 install --upgrade pip setuptools
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
CMD [ "bash", "start" ]
