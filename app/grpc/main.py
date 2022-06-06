import time
from concurrent import futures

import grpc
import service_pb2
import service_pb2_grpc


class LocationServicer(service_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        print("Received a message!")

        request_value = {
            "id": request.id,
            "person_id": request.person_id,
            "longitude": request.longitude,
            "latitude": request.latitude,
            "creation_time": request.creation_time
        }
        print(request_value)
        # TODO: create db with kafka

        return service_pb2.LocationMessage(**request_value)


class PersonServicer(service_pb2_grpc.PersonServiceServicer):
    def Create(self, request, context):
        print("Received a message!")

        request_value = {
            "id": request.id,
            "first_name": request.first_name,
            "last_name": request.last_name,
            "company_name": request.company_name,
        }
        print(request_value)
        # TODO: create db with kafka

        return service_pb2.PersonMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
service_pb2_grpc.add_LocationServiceServicer_to_server(
    LocationServicer(), server)
service_pb2_grpc.add_PersonServiceServicer_to_server(PersonServicer(), server)

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
