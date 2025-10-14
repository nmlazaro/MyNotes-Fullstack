from fastapi import FastAPI
from routes import notes_routes

app = FastAPI()

app.include_router(notes_routes.router)

@app.get("/")
def read_root():
    return {"message": "This is my FastAPI Backend :)"} # Change later