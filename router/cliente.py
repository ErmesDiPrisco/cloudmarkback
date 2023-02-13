from fastapi import APIRouter, status , HTTPException   

from dao.clientedao import Cliente_dao

from models.cliente import Cliente_model

from typing import List

router = APIRouter(prefix='/cliente', tags=['cliente'])


@router.get(
    '/all',
    response_model=List[Cliente_model],
    response_model_exclude_none=True,
    response_model_include={'id_cliente', 'nome', 'p_iva', 'indirizzo', 'cap', 'iban', 'telefono', 'email', 'pec', 'fax'})
async def get_cliente():
    return Cliente_dao.get_all_customers()

@router.get(
    '/customer',
    response_model=Cliente_model,
    response_model_exclude_none=True,
    response_model_include={'id_cliente', 'nome', 'p_iva', 'indirizzo', 'cap', 'iban', 'telefono', 'email', 'pec', 'fax'})
async def get_cliente(id: str):
    return Cliente_dao.get_customer_by_id(id)

@router.post('/new')
async def addCustomer(customer :Cliente_model):
  #return Cliente_dao.insert_customer(customer.id_cliente, customer.nome, customer.p_iva, customer.indirizzo,
                                       # customer.cap, customer.iban, customer.telefono, customer.email, customer.pec, customer.fax)
    return customer

@router.put('/update')
async def updateCustomer(customer: Cliente_model):
    return Cliente_dao.update_customer(customer.id_cliente, customer.nome, customer.p_iva, customer.indirizzo,
                                        customer.cap, customer.iban, customer.telefono, customer.email, customer.pec, customer.fax)

@router.delete('/delete')
async def deleteCustomer(customer: str):
    return Cliente_dao.delete_customer(customer)

@router.patch('/patch')
async def patchCustomer(customer: Cliente_model):
    return Cliente_dao.update_customer(customer.id_cliente, customer.nome, customer.p_iva, customer.indirizzo,
                                        customer.cap, customer.iban, customer.telefono, customer.email, customer.pec, customer.fax)
    
@router.get(
    'customer_by_id_azienda',
    response_model=List[Cliente_model],
    response_model_exclude_none=True,
    response_model_include={'id_cliente', 'nome', 'p_iva', 'indirizzo', 'cap', 'iban', 'telefono', 'email', 'pec', 'fax'})
async def get_clienti_by_azienda(id: str):
    return Cliente_dao.get_all_customers_by_id_azienda(id)

@router.get(
    'customer_by_commessa',
    response_model=List[Cliente_model],
    response_model_exclude_none=True,
    response_model_include={'id_cliente', 'nome', 'p_iva', 'indirizzo', 'cap', 'iban', 'telefono', 'email', 'pec', 'fax'})
async def get_clienti_by_commessa(id: str):
    return Cliente_dao.get_customers_by_commessa()