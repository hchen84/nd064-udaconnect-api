#!/bin/bash
KAFKA_HOME=$1

# start zookeeper
$KAFKA_HOME/bin/zookeeper-server-start.sh $KAFKA_HOME/config/zookeeper.properties &
# start kafka broker
$KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties &
# create topic "location"
$KAFKA_HOME/bin/kafka-topics.sh --create --topic location --bootstrap-server localhost:9092
$KAFKA_HOME/bin/kafka-topics.sh --create --topic person --bootstrap-server localhost:9092
# restart kafka broker
# $KAFKA_HOME/bin/kafka-server-stop.sh
# $KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties &
python -u consumer.py