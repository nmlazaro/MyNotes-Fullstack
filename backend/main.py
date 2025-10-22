from fastapi import FastAPI
from routes import notes_routes
from database import engine
from models import notes_models

notes_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(notes_routes.router)

@app.get("/")
def read_root():
    return {"message": "This is my FastAPI Backend :)"} # Change later