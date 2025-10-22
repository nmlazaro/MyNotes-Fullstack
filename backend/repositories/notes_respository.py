from sqlalchemy.orm import Session
from models import notes_models
from schemas import notes_schemas

def get_all_notes(db: Session):
    try:
        return db.query(notes_models.Note).all()
    except Exception as err:
        print(f'Error trying to get_all_notes -> ERROR: {err}')
        return []
    
def create_note(db: Session, note: notes_schemas.NoteCreate):
    db_note = notes_models.Note(**note.model_dump())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    
    return db_note