FROM ubuntu:20.04 as builder
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN apt update && apt install --no-install-recommends -y \
    curl \
    python3 \
    vim \
    net-tools \
    python3-pip \
    && pip install --upgrade pip \
       pip install -r ./requirements.txt
COPY . /usr/src/app/
ENTRYPOINT [ "python3", "app.py" ]
       
