from typing import List, Dict
from schemas import note_schemas

# Just for testing purposes. CHANGE LATER
db_notes: Dict[int, note_schemas.Note] = {
    1: note_schemas.Note(id=1, title='First Note', content='this is a random note'),
    2: note_schemas.Note(id=2, title='Grocery list', content='eggs, milk, bread')
}
next_id = 3

def get_all_notes() -> List[note_schemas.Note]:
    return list(db_notes.values())

def create_new_note(note_data: note_schemas.NoteCreate) -> note_schemas.Note:
    global next_id
    new_note = note_schemas.Note(id=next_id, **note_data.model_dump())
    db_notes[new_note.id] = new_note
    next_id += 1
    return new_note