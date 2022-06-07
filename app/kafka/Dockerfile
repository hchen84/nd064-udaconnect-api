FROM python:3.8
LABEL maintainer="Chen"

# ENV KAFKA_HOME /kafka
# ADD ./start-kafka.sh /scripts/
# WORKDIR .

COPY ./app/kafka /kafka
WORKDIR /kafka

RUN pip install -r requirements.txt

EXPOSE 9092
CMD ["python", "-u", "consumer.py"]