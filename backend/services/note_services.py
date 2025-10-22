from sqlalchemy.orm import Session
from schemas import notes_schemas
from repositories import notes_respository

def get_all_notes(db: Session):
    return notes_respository.get_all_notes(db=db)

def create_new_note(db: Session, note_data: notes_schemas.NoteCreate):
    return notes_respository.create_note(db=db, note=note_data)