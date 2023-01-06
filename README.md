# Technical test Pablo Ramírez for Gigflow

Implementation of REST API for find a Service and to list Services

> **_NOTE:_**  I will be performing the unit tests later, as it is currently the early morning hours and I have only had this time to do the test.

## Requirements
- Python 3.8

## Features
- SQLAlchemy
- Pydantic
- Docker
- Tests

## Usage

1. Initialize and active a virtual environment:
```bash
python3 -m venv venv
source ./venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
poetry install
```

3. Configure and run migrations:
   1. Create `.env` file  
   2. set environment variable `DATABASE_URL` with database url
   3. Run migrations
```bash
alembic upgrade heads
```

4. (Optional) Run seeds:
```bash
poetry run seeds
```

5. Run the development server:
```bash
poetry run server
```

6. View the API docs:
```bash
http://localhost:8000/docs
```

## Quick Start (Docker)
1. Build:
    ```bash
    docker-compose build
    ```

2. Run the app:
    ```bash
    docker-compose up -d
    ```

3. View the API docs:
    ```bash
    http://localhost:9090/docs
    ```
