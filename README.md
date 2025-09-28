# FastAPI Starter

A production-ready FastAPI starter project with built-in observability using OpenTelemetry.

## Features

- 🚀 FastAPI with modern Python development practices
- 📊 **OpenTelemetry Integration** - Distributed tracing, metrics, and observability out of the box
- 🐳 **Docker & Docker Compose** - Container-ready with observability stack
- 🔧 Built with `uv` for fast dependency management
- 📈 Production-ready configuration

## Quick Start (Recommended)

The fastest way to get started is using Docker Compose, which sets up both the API and observability infrastructure:

```shell
docker-compose up --build
```

This will start:
- **FastAPI application** on `http://localhost:8000`
- **OpenTelemetry Collector** on ports `4317` (gRPC) and `4318` (HTTP)

The API will automatically instrument and send traces and metrics to the collector.

## Local Development Setup

### Prerequisites
- Python 3.13+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager

### Quick Setup
1. **Clone and setup environment:**
   ```shell
   # Create virtual environment
   uv venv
   
   # Activate virtual environment
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   
   # Install dependencies
   uv sync
   ```

2. **Run the application:**
   ```shell
   # Simple start (recommended for development)
   python src/app.py
   
   # Or with uvicorn directly (with hot reload)
   uvicorn rest_api.main:app --reload --port 8000 --host 0.0.0.0 --app-dir src
   ```

3. **Verify it's working:**
   - Hello endpoint: http://localhost:8000/api/hello
   - API docs: http://localhost:8000/docs
   - OpenAPI spec: http://localhost:8000/openapi.json

### Development with OpenTelemetry
To test observability features locally, use the startup script:
```shell
OTEL_ENABLED=true OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317 ./start.sh
```
(Requires running the OpenTelemetry collector separately - see Docker Compose section for easier setup)

## OpenTelemetry Observability

This project includes comprehensive observability features:

### What's Instrumented
- **HTTP requests** - Automatic tracing of all API endpoints
- **Database queries** - If you add database integrations
- **External service calls** - HTTP clients, etc.
- **Custom metrics** - Application-specific metrics

### Configuration
OpenTelemetry is controlled via environment variables:
- `OTEL_ENABLED=true` - Enables automatic instrumentation
- `OTEL_EXPORTER_OTLP_ENDPOINT` - Where to send telemetry data

### Viewing Traces and Metrics
In the default setup, traces and metrics are logged to the console by the collector. For production, you would typically configure the collector to export to:
- **Jaeger** for distributed tracing
- **Prometheus** for metrics
- **Your observability platform** (DataDog, New Relic, etc.)

## Docker Deployment

### Docker Compose - Simple Start (Recommended)
```shell
# Start the full stack (API + observability)
docker-compose up --build
```

This will start both services in the foreground. You'll see logs from both the FastAPI app and OpenTelemetry collector. Press `Ctrl+C` to stop both services.

### Docker Compose - Background/Detached Mode
For production-like usage or if you prefer running services in the background:

```shell
# Start services in background (detached mode)
docker-compose up -d --build

# View logs from just the FastAPI app (recommended)
docker-compose logs -f fastapi-starter-app

# View logs from all services (includes verbose OpenTelemetry logs)
docker-compose logs -f

# Stop services
docker-compose down
```

The `fastapi-starter-app` log filtering is particularly useful since it excludes the verbose OpenTelemetry collector logs.

### Single Container
If you prefer to run just the API container:

```shell
# Build the image
docker build -t fastapi_starter_img .

# Run without OpenTelemetry
docker run -it -p 8000:8000 fastapi_starter_img

# Run with OpenTelemetry (requires external collector)
docker run -it -p 8000:8000 \
  -e OTEL_ENABLED=true \
  -e OTEL_EXPORTER_OTLP_ENDPOINT=http://your-collector:4317 \
  fastapi_starter_img
```


