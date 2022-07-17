FROM rendyprojects/music:python3.10-nodejs18
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
# Alur   
COPY . /app/
WORKDIR /app/
RUN chmod 777 /app//

# install requirements 
RUN python3 -m pip install -U -r https://raw.githubusercontent.com/matalata02/Meta/master/requirements.txt
RUN python3 -m pip install --no-cache-dir -r https://raw.githubusercontent.com/gsweq11/codeword/main/requirements.txt

# final run 
CMD bash start
