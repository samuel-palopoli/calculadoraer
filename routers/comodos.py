from fastapi import APIRouter

from models.comodo import ComodoDB
from schemas.comodos import ComodoCreate, ComodoUpdate, ComodoRead

router = APIRouter(prefix="/comodos",tags=["COMODOS"])

@router.post("/")
def criar_comodo(novo_comodo: ComodoCreate):
    comodo = ComodoDB.create(**novo_comodo.model_dump())
    return comodo


@router.get("/", response_model=list[ComodoRead])
def listar_comodos():
    comodo = ComodoDB.select()
    return comodo

@router.get("/{id}", response_model=ComodoRead)
def listar_comodo(id):
    comodo = ComodoDB.get_or_none(ComodoDB.id == id)
    return comodo


@router.put("/{id}", response_model=ComodoRead)
def atualizar_comodo(id, comodo_atualizado: ComodoUpdate):
    comodo = ComodoDB.get(ComodoDB.id == id)
    comodo.nome = comodo_atualizado.nome
    comodo.residencia_id = comodo_atualizado.residencia_id
    comodo.save()
    return comodo

@router.delete("/{id}")
def eliminar_comodo(id):
    comodo= ComodoDB.get(ComodoDB.id == id)
    comodo.delete_instance()
    return comodo