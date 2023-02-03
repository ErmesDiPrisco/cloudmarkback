from dao.utilities.db import Mysql
from models.dipendente import Dipendente_model

class Dipendente_dao:
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
        
        