from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from schemas import notes_schemas
from services import note_services
from sqlalchemy.orm import Session
from database import get_db


router = APIRouter()

# CRUD
# Read
@router.get("/notes", response_model=List[notes_schemas.Note])
def get_notes(db: Session = Depends(get_db)):
    return note_services.get_all_notes(db=db)

# Create
@router.post("/notes", response_model=notes_schemas.Note, status_code=status.HTTP_201_CREATED)
def create_note(note: notes_schemas.NoteCreate, db: Session = Depends(get_db)):
    return note_services.create_new_note(db=db, note_data=note)

# Read (ID)
@router.get("/notes/{note_id}", response_model=notes_schemas.Note)
def get_note_by_id(note_id: int, db: Session = Depends(get_db)):
    db_note = note_services.get_note(db=db, note_id=note_id)

    if db_note is None:
        raise HTTPException(status_code=404, detail='Note not found')
    
    return db_note

# Update
@router.put("/notes/{note_id}", response_model=notes_schemas.Note)
def update_note_by_id(note_id: int, note_update: notes_schemas.NoteUpdate, db: Session = Depends(get_db)):
    updated_note = note_services.update_note(db=db, note_id=note_id, note_update=note_update)

    if updated_note is None:
        raise HTTPException(status_code=404, detail='Note not found')
    
    return updated_note

# Delete
@router.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note_by_id(note_id: int, db: Session = Depends(get_db)):
    result = note_services.delete_note(db=db, note_id=note_id)
    if result is None:
        raise HTTPException(status_code=404, detail='Note not found')
    
    return