FROM ubuntu:latest


#RUN apt update
#RUN apt install python3 -y
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.5 \
    python3-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install aiofiles


WORKDIR /usr/app/src

COPY . ./

CMD ["python3","JsonParsingAsync.py"]



