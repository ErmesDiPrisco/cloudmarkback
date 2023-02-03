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
            results.append(Azienda_model(id_azienda=element[0], nome=element[1], p_iva=element[2], 
            indirizzo=element[3], cap=element[4], iban=element[5], telefono=element[6], email=element[7], pec=element[8], fax=element[9] ))
        Mysql.close_connection()
        return results
    # company by id
     # employee by id
    def get_company_by_id(cls, id):
        Mysql.openconnection()
        Mysql.query(f'SELECT * FROM azienda WHERE id_azienda = {id}')
        data = Mysql.get_results()
        results = list()
        for element in data:
            results.append(Azienda_model(id_dipendente = element[0], nome = element[1], cognome = element[2], 
                                            cf = element[3], iban = element[4], id_tipo_contratto = element[5], 
                                            email = element[6], telefono = element[7], data_nascita = element[8]))
        Mysql.close_connection()
        return results
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
        Mysql.close_connection()
    # UPDATE
    @classmethod
    def update_company(cls, id_azienda, nome, p_iva, indirizzo, cap, iban, telefono, email, pec, fax):
        Mysql.openconnection()
        Mysql.query(f"UPDATE azienda\
                    SET nome='{nome}', p_iva= '{p_iva}', indirizzo= '{indirizzo}', cap='{cap}', iban='{iban}', telefono='{telefono}', email='{email}', pec='{pec}', fax='{fax}'\
                        WHERE id_azienda={id_azienda}")
        Mysql.close_connection()