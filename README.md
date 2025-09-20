# fastapi-starter
A production-ready FastAPI starter project

## Local Setup
### System requirements
- Python 3.13
- uv

### Install project dependencies
If the virtual environment is not already created, it can be created with:
```shell
python -m venv .venv
```
or
```shell
uv venv
```

To install the project's dependencies in the virtual environment,
run the following command:
```shell
uv sync
```

### Running locally
From the project's root directory, you may launch the API locally.

#### With uvicorn
```shell
uvicorn rest_api.main:app --port 8000 --host 0.0.0.0 --app-dir src
```
#### As Python script
```shell
python src/app.py
```

## Docker container management

### Running a docker container locally
It's possible to run the API locally as a docker container.
#### 1. Create Docker image 
```shell
docker build -t fastapi_starter_img .
```
#### 2. Run Docker image
```shell
docker run -it -p 8000:8000 [--name my_api] fastapi_starter_img
```

