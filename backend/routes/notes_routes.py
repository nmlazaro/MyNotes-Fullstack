from fastapi import APIRouter
from typing import List
from schemas import note_schemas
from services import note_services

router = APIRouter()

@router.get("/notes", response_model=List[note_schemas.Note])
def get_notes():
    return note_services.get_all_notes()

@router.post("/notes", response_model=note_schemas.Note)
def create_note(note: note_schemas.NoteCreate):
    return note_services.create_new_note(note_data=note)