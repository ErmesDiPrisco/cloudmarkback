from dao.utilities.db import Mysql
from models.cliente import Cliente_model

class Cliente_dao:
    # all customers
    @classmethod
    def get_all_customers(cls):
        Mysql.openconnection()
        Mysql.query('select * from cliente')
        data= Mysql.get_results()
        results=list()
        for element in data:
            results.append(Cliente_model(**element))
        Mysql.close_connection()
        return results
 # customer by id
    @classmethod
    def get_customer_by_id(cls, id):
        Mysql.openconnection()
        Mysql.query(f'SELECT * FROM cliente WHERE id_cliente = \'{id}\'')
        data = Mysql.get_results()
        result = Cliente_model(**data[0])
        # for element in data:
        #     result.append(cliente_model(**element))
        Mysql.close_connection()
        return result
    # INSERT
    @classmethod
    def insert_customer(cls, id_cliente, nome, p_iva, indirizzo, cap, iban, telefono, email, pec, fax):
        Mysql.openconnection()
        Mysql.query(f"INSERT INTO cliente (id_cliente, nome, p_iva, indirizzo, cap, iban, telefono, email, pec, fax) \
                        VALUE ('{id_cliente}','{nome}','{p_iva}','{indirizzo}','{cap}','{iban}','{telefono}','{email}','{pec}','{fax}')")
        Mysql.commit()
        Mysql.close_connection()
    # DELETE
    @classmethod
    def delete_customer(cls, id_cliente):
        Mysql.openconnection()
        Mysql.query(f'DELETE from cliente where id_cliente="{id_cliente}"')
        Mysql.commit()
        Mysql.close_connection()
    # UPDATE
    @classmethod
    def update_customer(cls, id_cliente, nome, p_iva, indirizzo, cap, iban, telefono, email, pec, fax):
        Mysql.openconnection()
        Mysql.query(f"UPDATE cliente\
                    SET nome='{nome}', p_iva= '{p_iva}', indirizzo= '{indirizzo}', cap='{cap}', iban='{iban}', telefono='{telefono}', email='{email}', pec='{pec}', fax='{fax}'\
                        WHERE id_cliente='{id_cliente}'")
        Mysql.commit()
        Mysql.close_connection()
        
    @classmethod
    def get_all_customers_by_id_azienda(cls):
        Mysql.openconnection()
        Mysql.query('select * from azienda_cliente')
    Mysql.commit()
    Mysql.close_connection()
    
    @classmethod
    def get_customers_by_commessa(cls):
        Mysql.openconnection()
        Mysql.query('SELECT id_cliente, nome, p_iva, indirizzo, cap, iban, telefono, email, pec, fax \
                    FROM cliente c \
                    INNER JOIN commessa cm ON c.id_cliente = cm.id_cliente') 