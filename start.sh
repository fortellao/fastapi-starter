#!/bin/sh

if [ "$OTEL_ENABLED" = "true" ]; then
  echo "Starting with OpenTelemetry instrumentation..."
  exec uv run opentelemetry-instrument \
    --metrics_exporter otlp \
    --traces_exporter otlp \
    --logs_exporter none \
    uvicorn rest_api.main:app --port 8000 --host 0.0.0.0 --app-dir src
else
  echo "Starting without OpenTelemetry instrumentation..."
  exec uvicorn rest_api.main:app --port 8000 --host 0.0.0.0 --app-dir src
fi