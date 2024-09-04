from fastapi import APIRouter

from models.residencia import ResidenciaDB
from schemas.residencia import ResidenciaCreate, ResidenciaRead, ResidenciaUpdate

router = APIRouter(prefix="/residencias",tags=["RESIDÊNCIAS"])

@router.post("/")
def criar_residencia(nova_residencia: ResidenciaCreate):
    residencia = ResidenciaDB.create(**nova_residencia.model_dump())
    return residencia

@router.get("/", response_model=list[ResidenciaRead])
def listar_residencias():
    residencias = ResidenciaDB.select()
    return residencias

@router.get("/{id}", response_model=ResidenciaRead)
def listar_residencia(id):
    residencia = ResidenciaDB.get_or_none(ResidenciaDB.id == id)
    return residencia


@router.put("/{id}", response_model=ResidenciaRead)
def atualizar_residencia(id, residencia_atualizada: ResidenciaUpdate):
    residencia = ResidenciaDB.get(ResidenciaDB.id == id)
    residencia.proprietario = residencia_atualizada.proprietario
    residencia.save()
    return residencia

@router.delete("/{id}")
def eliminar_residencia(id):
    residencia = ResidenciaDB.get(ResidenciaDB.id == id)
    residencia.delete_instance()
    return residencia