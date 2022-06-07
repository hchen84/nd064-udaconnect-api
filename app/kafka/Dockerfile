FROM openjdk:8-jdk-alpine3.9
ENV KAFKA_HOME /kafka
# ADD ./start-kafka.sh /scripts/
# WORKDIR .

COPY ./app/kafka /kafka
WORKDIR /kafka

# install some basic tools
RUN apk add wget --no-cache curl tar bash procps
# install kafka (pick latest stable version here)

RUN wget https://dlcdn.apache.org/kafka/3.2.0/kafka_2.13-3.2.0.tgz && \
    tar -xzf kafka_2.13-3.2.0.tgz && \
    mv kafka_2.13-3.2.0.tgz /kafka

EXPOSE 9092
CMD ["./start-kafka.sh", "/kafka"]