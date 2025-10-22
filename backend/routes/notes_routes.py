from fastapi import APIRouter, Depends
from typing import List
from schemas import notes_schemas
from services import note_services
from sqlalchemy.orm import Session
from database import get_db


router = APIRouter()

@router.get("/notes", response_model=List[notes_schemas.Note])
def get_notes(db: Session = Depends(get_db)):
    return note_services.get_all_notes(db=db)

@router.post("/notes", response_model=notes_schemas.Note)
def create_note(note: notes_schemas.NoteCreate, db: Session = Depends(get_db)):
    return note_services.create_new_note(db=db, note_data=note)