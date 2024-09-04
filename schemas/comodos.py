
from pydantic import BaseModel, Field

class ComodoCreate(BaseModel):
    nome: str
    residencia_id: int

class ComodoRead(BaseModel):
    id: int
    nome: str
    residencia_id: int

class ComodoUpdate(BaseModel):
    nome: str
    residencia_id: int
