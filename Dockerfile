FROM docker.io/bitnami/spark:3.2.0-debian-10-r3

COPY spark-executor.py /opt/bitnami/spark/examples/spark-executor.py

USER root
