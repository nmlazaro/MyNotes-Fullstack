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

def get_note_by_id(db: Session, note_id: int):
    return db.query(notes_models.Note).filter(notes_models.Note.id == note_id).first()

def update_note_db(db: Session, note: notes_models.Note, note_update: notes_schemas.NoteUpdate):
    update_data = note_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(note, key, value)
    
    db.add(note)
    db.commit()
    db.refresh(note)

    return note

def delete_note_db(db: Session, note: notes_models.Note): # TODO Should change this later to logic delete
    db.delete(note)
    db.commit()

    return True


