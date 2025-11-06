FROM python:3.11-slim
WORKDIR /app
RUN pip install prometheus_client
COPY custom_exporter.py .
CMD ["python", "custom_exporter.py"]
