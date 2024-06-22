FROM python:3.10-slim
RUN apt-get update && apt-get install -y iputils-ping
WORKDIR /app
COPY . .
ENTRYPOINT ["python3", "mtu.py"]
