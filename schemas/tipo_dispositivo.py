from pydantic import BaseModel


class TipoDispositivoCreate(BaseModel):
    nome: str


class TipoDispositivoUpdate(BaseModel):
    nome: str


class TipoDispositivoRead(BaseModel):
    id: int
    nome: str


class TipoDispositivoReadList(BaseModel):
    tipo_dispositivos: list[TipoDispositivoRead]