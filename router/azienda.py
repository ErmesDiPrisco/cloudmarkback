from fastapi import APIRouter, status

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
