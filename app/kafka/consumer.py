from kafka import KafkaConsumer


def process_topic_loaction(msg):
    print("location:", msg)


def process_topic_person(msg):
    print("person:", msg)


def serve():
    consumer = KafkaConsumer()
    consumer.subscribe(['location', 'person'])

    func_dict = {"location": process_topic_loaction,
                 "person": process_topic_person}

    while True:
        msg = consumer.poll(1.0)

        if msg is None or len(msg) == 0:
            continue

        for tp, messages in msg.items():
            for message in messages:
                func_dict[tp.topic](message.value)


if __name__ == '__main__':
    serve()
