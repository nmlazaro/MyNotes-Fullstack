from pydantic import BaseModel, ConfigDict
from typing import Optional

class NoteCreate(BaseModel):
    title: str
    content: str

class Note(NoteCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)

class NoteUpdate(BaseModel): # Optionals when editing
    title: Optional[str] = None
    content: Optional[str] = None