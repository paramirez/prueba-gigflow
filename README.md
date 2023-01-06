# Technical test Pablo Ramírez for Gigflow

Implementation of REST API for find a Service and to list Services

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