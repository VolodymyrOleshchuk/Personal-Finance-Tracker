from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings

# Database URL from config
DATABASE_URL = settings.DATABASE_URL

# Extra config for SQLite (needed for multithreading)
connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

# Create database engine
engine = create_engine(DATABASE_URL, connect_args=connect_args)

# Session factory (used to interact with DB)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for models
Base = declarative_base()


# Dependency for getting DB session in routes
def get_db():
    db = SessionLocal()
    try:
        yield db  # give session to endpoint
    finally:
        db.close()  # always close session