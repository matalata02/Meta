FROM nikolaik/python-nodejs:python3.10-nodejs17
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN git clone -b master https://github.com/matalata02/Meta/
COPY . /app/
WORKDIR /app/
RUN python3 -m pip install --no-cache-dir -r https://raw.githubusercontent.com/gsweq11/codeword/main/requirements.txt
CMD [ "bash", "start" ]
