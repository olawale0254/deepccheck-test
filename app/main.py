from fastapi import FastAPI
from .models import Base
from .database import engine
from .routes import router as api_router

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# API routes
app.include_router(api_router)
