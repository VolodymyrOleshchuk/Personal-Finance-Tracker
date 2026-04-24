from fastapi import FastAPI

from app.core.database import Base, engine
from app.models.user import User
from app.models.category import Category
from app.models.transaction import Transaction

from app.api.routes.auth import router as auth_router
from app.api.routes.users import router as users_router
from app.api.routes.categories import router as categories_router
from app.api.routes.transactions import router as transactions_router
from app.api.routes.analytics import router as analytics_router

app = FastAPI(title="Personal Finance Tracker")

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(categories_router)
app.include_router(transactions_router)
app.include_router(analytics_router)

@app.get("/")
def root():
    return {"message": "Personal Finance Tracker API is running"}