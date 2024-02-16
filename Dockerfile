# Use the official Ubuntu base image
#FROM ubuntu:latest
FROM python:3.9-alpine

# Update package lists and install Python 3
# RUN apt-get update && \
#     apt-get install -y vim && \
#     apt-get install -y python3 && \
RUN  rm -rf /var/lib/apt/lists/*
    

# Create the directory /home/data
RUN mkdir -p /home/data

WORKDIR /home/data
COPY Project3.py ./


# Mount the local directory to /home/data in the container
#VOLUME ["/Users/abhiacherjee/Desktop/Docker_Exercise"]

CMD ["python3", "/home/data/Project3.py"]
