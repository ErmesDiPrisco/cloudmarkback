from fastapi import APIRouter, status , HTTPException   

from dao.dipendente_dao import Dipendente_dao

from models.dipendente import Dipendente_model

from typing import List

router = APIRouter(prefix='/dipendente', tags=['dipendente'])


@router.get(
    '/all',
    response_model=List[Dipendente_model],
    response_model_exclude_none=True,
    response_model_include={'id_dipendente', 'nome', 'cognome', 'cf', 'iban', 'id_tipo_contratto', 'email', 'telefono', 'data_nascita'})
async def get_dipendente():
    return Dipendente_dao.get_all_employees()


@router.get("")
async def prendi_dipendente(id_dipendente: str | None=None):
    if id_dipendente:
        if Dipendente_dao.get_all_employees(id_dipendente) == None :
            raise HTTPException (status_code=404, detail="Dipendente non trovato")
        try: 
            if Dipendente_dao.get_all_employees() == []:
                raise HTTPException (status_code=404, detail="Dipendente non trovato")
        except Exception as e:
            raise HTTPException (status_code=500, detail=e.msg)