FROM openjdk:8-jdk-alpine3.9

LABEL maintainer="Chen"

# ENV KAFKA_HOME /kafka
# ADD ./start-kafka.sh /scripts/
# WORKDIR .

COPY ./app/kafka /kafka
WORKDIR /kafka

# install some basic tools
RUN apk add wget --no-cache curl tar bash procps
# install kafka (pick latest stable version here)

RUN wget https://dlcdn.apache.org/kafka/3.2.0/kafka_2.13-3.2.0.tgz && \
    tar -xzf kafka_2.13-3.2.0.tgz && \
    rm kafka_2.13-3.2.0.tgz
# mv kafka_2.13-3.2.0.tgz /kafka

RUN apk add --no-cache python3 \
    && python3 -m ensurepip \
    && pip3 install --upgrade pip setuptools \
    && rm -r /usr/lib/python*/ensurepip && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

RUN pip install -r requirements.txt

EXPOSE 9092
CMD ["./start-kafka.sh", "./kafka_2.13-3.2.0"]