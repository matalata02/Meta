FROM nikolaik/python-nodejs:python3.10-nodejs18
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get autoremove --purge
RUN pip3 install --upgrade pip setuptools 
RUN if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi 
RUN if [ ! -e /usr/bin/python ]; then ln -sf /usr/bin/python3 /usr/bin/python; fi 
RUN rm -r /root/.cache
RUN git clone -b master https://github.com/matalata02/Meta /root/Meta
RUN mkdir /root/Meta/bin/
WORKDIR /root/Meta/
RUN chmod +x /usr/local/bin/*
    
# Alur   
COPY . /app/
WORKDIR /app/
RUN chmod 777 /app//

# install requirements 
RUN python3 -m pip install -U -r  https://raw.githubusercontent.com/matalata02/Meta/master/requirements.txt
RUN python3 -m pip install --no-cache-dir -r https://raw.githubusercontent.com/gsweq11/codeword/main/requirements.txt

# final run 
CMD ["bash", "startup.sh"]
