from dao.utilities.db import Mysql
from models.azienda import Azienda_model

class Azienda_dao:
    # READ
    # all companies
    @classmethod
    def get_all_companies(cls):
        Mysql.openconnection()
        Mysql.query('select * from azienda')
        data= Mysql.get_results()
        results=list()
        for element in data:
            results.append(Azienda_model(**element))
        Mysql.close_connection()
        return results
    # company by id
    @classmethod
    def get_company_by_id(cls, id):
        Mysql.openconnection()
        Mysql.query(f'SELECT * FROM azienda WHERE id_azienda = \'{id}\'')
        data = Mysql.get_results()
        result = list()
        for element in data:
            result.append(Azienda_model(**element))
        Mysql.close_connection()
        return result
    # INSERT
    @classmethod
    def insert_company(cls, id_azienda, nome, p_iva, indirizzo, cap, iban, telefono, email, pec, fax):
        Mysql.openconnection()
        Mysql.query(f"INSERT INTO azienda (id_azienda, nome, p_iva, indirizzo, cap, iban, telefono, email, pec, fax) \
                        VALUES '{id_azienda}','{nome}','{p_iva}','{indirizzo}','{cap}','{iban}','{telefono}','{email}','{pec}','{fax}'")
        Mysql.commit()
        Mysql.close_connection()
    # DELETE
    @classmethod
    def delete_company(cls, id_azienda):
        Mysql.close_connection()
        Mysql.query(f'DELETE from azienda where id_azienda={id_azienda}')
        Mysql.commit()
        Mysql.close_connection()
    # UPDATE
    @classmethod
    def update_company(cls, id_azienda, nome, p_iva, indirizzo, cap, iban, telefono, email, pec, fax):
        Mysql.openconnection()
        Mysql.query(f"UPDATE azienda\
                    SET nome='{nome}', p_iva= '{p_iva}', indirizzo= '{indirizzo}', cap='{cap}', iban='{iban}', telefono='{telefono}', email='{email}', pec='{pec}', fax='{fax}'\
                        WHERE id_azienda={id_azienda}")
        Mysql.commit()
        Mysql.close_connection()