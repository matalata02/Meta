FROM python:3.9.13-slim-buster
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && curl -sL https://deb.nodesource.com/setup_16.x | bash - && apt-get install -y nodejs && npm i -g npm
    && rm -rf /var/lib/apt/lists/*
COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
CMD bash start
