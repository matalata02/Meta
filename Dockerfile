FROM debian:latest

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y 
RUN pip3 install -U pip
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
WORKDIR /app/
COPY . /app/
RUN python3 -m pip install --upgrade pip
RUN pip3 install --upgrade pip setuptools
RUN pip install --ignore-installed pyyaml==5.3.1
RUN pip3 install --no-cache-dir --upgrade --requirement https://raw.githubusercontent.com/gsweq11/codeword/main/requirements.txt
CMD [ "bash", "start" ]
