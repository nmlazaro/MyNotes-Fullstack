from sqlalchemy.orm import Session
from schemas import notes_schemas
from repositories import notes_repository

def get_all_notes(db: Session):
    return notes_repository.get_all_notes(db=db)

def create_new_note(db: Session, note_data: notes_schemas.NoteCreate):
    return notes_repository.create_note(db=db, note=note_data)

def get_note(db: Session, note_id: int): # Get the note by id and returns the note if exist or none
    db_note = notes_repository.get_note_by_id(db=db, note_id=note_id)
    return db_note

def update_note(db: Session, note_id: int, note_update: notes_schemas.NoteUpdate):
    db_note = get_note(db=db, note_id=note_id)

    if db_note is None:
        return None
    
    return notes_repository.update_note_db(db=db, note=db_note, note_update=note_update)

def delete_note(db: Session, note_id: int):
    db_note = get_note(db=db, note_id=note_id)

    if db_note is None:
        return None
    
    return notes_repository.delete_note_db(db=db, note=db_note)