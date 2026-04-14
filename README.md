# FastAPI User Assignment

## Overview
This project enhances a FastAPI calculator app by adding a secure user model with SQLAlchemy, password hashing, testing, CI/CD, and Docker Hub deployment.

## Features
- Calculator APIs
- User Registration API
- Hashed Password Storage
- SQLAlchemy User Model
- Pydantic Validation
- Unit Tests
- Integration Tests
- GitHub Actions
- Docker Deployment

## Run Locally

```bash
pip install -r requirements.txt
pytest
uvicorn main:app --reload

