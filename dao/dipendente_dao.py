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
            print(element)
            results.append(Dipendente_model(**element))
        Mysql.close_connection()
        return results
    # employee by id
    @classmethod
    def get_employee_by_id(cls, id):
        Mysql.openconnection()
        Mysql.query(f'SELECT * FROM dipendente WHERE id_dipendente = \'{id}\'')
        data = Mysql.get_results()
        result = list()
        for element in data:
            result.append(Dipendente_model(**element))
        Mysql.close_connection()
        return result
    # get all employees by azienda_id
    @classmethod
    def get_all_emplyees_by_id_azienda(cls, id):
        Mysql.openconnection()
        Mysql.query(f"SELECT d.id_dipendente, d.nome, d.cognome, d_a.matricola, d.cf, d.iban, d.id_tipo_contratto, d.email, d.telefono, d.data_nascita \
                        FROM dipendente d \
                        INNER JOIN dipendente_azienda d_a ON d.id_dipendente = d_a.id_dipendente \
                        INNER JOIN azienda a ON d_a.id_azienda = a.id_azienda \
                        WHERE a.id_azienda = '{id}' \
                    ")
        data = Mysql.get_results()
        result = list()
        for element in data:
            result.append(Dipendente_model(**element))
        Mysql.close_connection()
        return result
    # find multi emplooyees
    @classmethod
    def find_multi_employees(cls, value: str, id: str):
        Mysql.openconnection()
        Mysql.query(f"SELECT d.id_dipendente, d.nome, d.cognome, d_a.matricola, d.cf, d.iban, d.id_tipo_contratto, d.email, d.telefono, d.data_nascita \
                        FROM dipendente d \
                        INNER JOIN dipendente_azienda d_a ON d.id_dipendente = d_a.id_dipendente \
                        INNER JOIN azienda a ON d_a.id_azienda = a.id_azienda \
                        WHERE d_a.matricola like '{value}%' \
                        OR d.nome like '{value}%' \
                        OR d.cognome like '{value}%' \
                        OR (concat(d.nome, ' ', d.cognome) like '{value}%')  \
                        OR (concat(d.cognome, ' ', d.nome) like '{value}%')  \
                    ")
        results = Mysql.get_results()
        Mysql.close_connection()
        return results
        
    # INSERT
    @classmethod
    def insert_employee(cls, id_dipendente, nome, cognome, cf, iban, id_tipo_contratto, email, telefono, data_nascita):
        Mysql.openconnection()
        Mysql.query(f"INSERT INTO dipendente (id_dipendente, nome, cognome, cf, iban, id_tipo_contratto, email, telefono, data_nascita) \
                        VALUES ('{id_dipendente}','{nome}','{cognome}','{cf}','{iban}','{id_tipo_contratto}','{email}','{telefono}','{data_nascita}')")
        Mysql.commit()
        Mysql.close_connection()
    # DELETE
    @classmethod
    def delete_employee(cls, id_dipendente):
        Mysql.openconnection()
        Mysql.query(f"DELETE from dipendente where id_dipendente='{id_dipendente}'")
        Mysql.commit()
        Mysql.close_connection()
    # UPDATE
    @classmethod
    def update_employee(cls, id_dipendente, nome, cognome, cf, iban, id_tipo_contratto, email, telefono, data_nascita):
        Mysql.openconnection()
        Mysql.query(f"UPDATE dipendente\
                    SET nome='{nome}', nome= '{nome}', cognome= '{cognome}', cf='{cf}', iban='{iban}', id_tipo_contratto='{id_tipo_contratto}', email='{email}', telefono='{telefono}', data_nascita='{data_nascita}'\
                        WHERE id_dipendente={id_dipendente}")
        Mysql.commit()
        Mysql.close_connection()
    
    @classmethod
    def link_employee_company(cls, id_dipendente, id_azienda, data_inizio_rapporto, matricola, data_fine_rapporto):
        Mysql.openconnection()
        Mysql.query(f"INSERT INTO dipendente_azienda (id_dipendente,id_azienda, data_inizio_rapporto, matricola,data_fine_rapporto)\
                    VALUES ('{id_dipendente}', '{id_azienda}','{data_inizio_rapporto}','{matricola}','{data_fine_rapporto}')")
        Mysql.commit()
        Mysql.close_connection()

    @classmethod
    def deletelink(cls, id_dipendente, id_azienda):
        Mysql.openconnection()
        Mysql.query(f"DELETE from dipendente_azienda where id_dipendente='{id_dipendente}' and id_azienda='{id_azienda}'")
        Mysql.commit()
        Mysql.close_connection()
        
        