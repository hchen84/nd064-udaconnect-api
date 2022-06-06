FROM python:3.8
LABEL maintainer="Hainan Chen"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ service.proto
# command to run on container start
CMD [ "python", "main.py" ]