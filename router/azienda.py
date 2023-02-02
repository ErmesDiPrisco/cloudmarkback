from fastapi import APIRouter, status , HTTPException   

from dao.aziendadao import Azienda_dao

from models.azienda import Azienda_model

from typing import List

router = APIRouter(prefix='/azienda', tags=['azienda'])


@router.get(
    '/all',
    response_model=List[Azienda_model],
    response_model_exclude_none=True,
    response_model_include={'id_azienda', 'nome', 'p_iva', 'indirizzo', 'cap', 'iban', 'telefono', 'email', 'pec', 'fax'})
async def get_aziende():
    return Azienda_dao.get_all_companies()


@router.get("")
async def prendi_azienda(azienda_id: str | None=None):
    if azienda_id:
        if Azienda_dao.get_all_companies(azienda_id) == None :
            raise HTTPException (status_code=404, detail="Azienda non trovata")
        try: 
            if Azienda_dao.get_all_companies() == []:
                raise HTTPException (status_code=404, detail="Azienda non trovata")
        except Exception as e:
            raise HTTPException (status_code=500, detail=e.msg)