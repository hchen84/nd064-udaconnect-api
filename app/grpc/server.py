import imp
import time
import logging

from concurrent import futures

import grpc
import service_pb2
import service_pb2_grpc
from kafka import KafkaProducer
import logging
import json

KAFKA_SERVER = 'localhost:9092'
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)


class LocationServicer(service_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        global producer
        print("Received a location message!")

        request_value = {
            "id": request.id,
            "person_id": request.person_id,
            "longitude": request.longitude,
            "latitude": request.latitude,
            "creation_time": request.creation_time
        }
        logging.info("location: " + request_value)
        data = json.dumps(request_value).encode()
        # TODO: create db with kafka

        TOPIC_NAME = 'location'
        producer.send(TOPIC_NAME, data)
        producer.flush()

        return service_pb2.LocationMessage(**request_value)


class PersonServicer(service_pb2_grpc.PersonServiceServicer):
    def Create(self, request, context):
        global producer
        print("Received a person message!")

        request_value = {
            "id": request.id,
            "first_name": request.first_name,
            "last_name": request.last_name,
            "company_name": request.company_name,
        }
        logging.info("person: " + request_value)
        # TODO: create db with kafka
        data = json.dumps(request_value).encode()
        TOPIC_NAME = 'person'
        producer.send(TOPIC_NAME, data)
        producer.flush()
        return service_pb2.PersonMessage(**request_value)


def serve():
    logging.basicConfig(
        handlers=[logging.StreamHandler()], format="%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s", level=logging.DEBUG,  datefmt="%Y-%m-%d %H:%M:%S")

    logging.info("Initialize gRPC server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    service_pb2_grpc.add_LocationServiceServicer_to_server(
        LocationServicer(), server)
    service_pb2_grpc.add_PersonServiceServicer_to_server(
        PersonServicer(), server)

    # TODO: server pod
    print("Server starting on port 5005...")
    server.add_insecure_port("[::]:5005")
    server.start()
    # Keep thread alive
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
