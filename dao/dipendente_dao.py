from dao.utilities.db import Mysql
from models.dipendente import Dipendente_model

class Dipendente_dao:
    # READ
    # all employees
    @classmethod
    def get_all_employees(cls):
        Mysql.openconnection()
        Mysql.query('SELECT * FROM dipendente')
        data = Mysql.get_results()
        results = list()
        for element in data:
            results.append(Dipendente_model(id_dipendente = element[0], nome = element[1], cognome = element[2], 
                                            cf = element[3], iban = element[4], id_tipo_contratto = element[5], 
                                            email = element[6], telefono = element[7], data_nascita = element[8]))
        Mysql.close_connection()
        return results
    # employee by id
    def get_employee_by_id(cls, id):
        Mysql.openconnection()
        Mysql.query(f'SELECT * FROM dipendente WHERE id_dipendente = {id}')
        data = Mysql.get_results()
        results = list()
        for element in data:
            results.append(Dipendente_model(id_dipendente = element[0], nome = element[1], cognome = element[2], 
                                            cf = element[3], iban = element[4], id_tipo_contratto = element[5], 
                                            email = element[6], telefono = element[7], data_nascita = element[8]))
        Mysql.close_connection()
        return results
    # find multi emplooyees
    def find_multi_employees(cls, value: str, id: str):
        Mysql.openconnection()
        Mysql.query(f"SELECT d.nome, d.cognome, d_a.matricola, d.cf \
                        FROM dipendente d \
                        INNER JOIN dipendente_azienda d_a ON d.id_dipendente = d_a.id_dipendente \
                        INNER JOIN azienda a ON d_a.id_azienda = a.id_azienda \
                        WHERE d_a.matricola like '{value}%' \
                        OR d.nome like '{value}%' \
                        OR d.cognome like '{value}%' \
                        AND d.id_azienda = '{id}' \
                    ")
        results = Mysql.get_results()
        Mysql.close_connection()
        return results
        
    # INSERT
    @classmethod
    def insert_employee(cls, id_dipendente, nome, cognome, cf, iban, id_tipo_contratto, email, telefono, data_nascita):
        Mysql.openconnection()
        Mysql.query(f"INSERT INTO dipendente (id_dipendente, nome, cognome, cf, iban, id_tipo_contratto, email, telefono, data_nascita) \
                        VALUES '{id_dipendente}','{nome}','{cognome}','{cf}','{iban}','{id_tipo_contratto}','{email}','{telefono}','{data_nascita}'")
        Mysql.commit()
        Mysql.close_connection()
    # DELETE
    @classmethod
    def delete_employee(cls, id_dipendente):
        Mysql.close_connection()
        Mysql.query(f'DELETE from dipendente where id_dipendente={id_dipendente}')
        Mysql.close_connection()
    # UPDATE
    @classmethod
    def update_employee(cls, id_dipendente, nome, cognome, cf, iban, id_tipo_contratto, email, telefono, data_nascita):
        Mysql.openconnection()
        Mysql.query(f"UPDATE dipendente\
                    SET nome='{nome}', nome= '{nome}', cognome= '{cognome}', cf='{cf}', iban='{iban}', id_tipo_contratto='{id_tipo_contratto}', email='{email}', telefono='{telefono}', data_nascita='{data_nascita}'\
                        WHERE id_dipendente={id_dipendente}")
        Mysql.close_connection()
        
        