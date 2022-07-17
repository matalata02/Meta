FROM nikolaik/python-nodejs:python3.8-nodejs18
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN git clone -b master https://github.com/matalata02/Meta/
COPY . /app/
WORKDIR /app/
RUN pip3 install -r https://raw.githubusercontent.com/matalata02/simple/main/requiremets.txt?token=GHSAT0AAAAAABWV5WWF5UGFO3OJD4SJXZNYYWTZRCA
CMD [ "bash", "start" ]
