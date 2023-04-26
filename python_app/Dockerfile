FROM ubuntu:20.04 as builder
WORKDIR /usr/src/app
COPY ./python_app/requirements.txt /usr/src/app
RUN apt update && apt install --no-install-recommends -y \
    curl \
    python3 \
    vim \
    net-tools \
    python3-pip \
    && pip install --upgrade pip \
       pip install -r ./requirements.txt
COPY /python_app /usr/src/app/
CMD [ "python3 app.py" ]
# FROM alpine as runner
# WORKDIR /usr/src/app
# COPY --from=builder /usr/src/app /usr/src/app/
# COPY --from=builder /usr/bin/ /usr/bin/
       
