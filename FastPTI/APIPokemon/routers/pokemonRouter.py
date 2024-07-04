from fastapi import  APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/pokedex")

class pokemon(BaseModel):
    dexNumb:int
    nome:str
    descricao:str


@router.get("/", response_model=List[pokemon])
def listPokemon():
    return [
        pokemon(
            dexNumb=1,
            nome="Bulbasaur",
            descricao="sapo planta"
        )
    ]



