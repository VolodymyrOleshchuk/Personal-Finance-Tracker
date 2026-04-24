# Personal Finance Tracker API

Backend API for managing personal finances using FastAPI.

## Features

- User registration and login
- JWT authentication
- Protected user endpoints
- Categories CRUD
- Transactions CRUD
- Analytics summary

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT
- Passlib / bcrypt

## API Endpoints

### Auth
- POST `/auth/register`
- POST `/auth/login`

### Users
- GET `/users/me`

### Categories
- GET `/categories`
- POST `/categories`
- PUT `/categories/{category_id}`
- DELETE `/categories/{category_id}`

### Transactions
- GET `/transactions`
- POST `/transactions`
- PUT `/transactions/{transaction_id}`
- DELETE `/transactions/{transaction_id}`

### Analytics
- GET `/analytics/summary`

## API Docs

http://127.0.0.1:8000/docs

## Run Locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Author

[Volodymyr Oleshchuk](https://github.com/VolodymyrOleshchuk)
