class Dipendente:
    def __init__(self, id_dipendente, nome, cognome, cf, iban, id_tipo_contratto, email, telefono, data_nascita):
        self.id_dipendente = id_dipendente
        self.nome = nome
        self.cognome = cognome 
        self.cf = cf
        self.iban = iban
        self.id_tipo_contratto = id_tipo_contratto
        self.email = email
        self.telefono = telefono
        self.data_nascita = data_nascita

    # id_dipendente getter & setter
    @property
    def id_dipendente(self):
        return self._id_dipendente
    
    @id_dipendente.setter
    def id_dipendente(self, id_dipendente):
        self._id_dipendente = id_dipendente
    # nome getter & setter
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    # cognome getter & setter
    @property
    def cognome(self):
        return self._cognome
    
    @cognome.setter
    def cognome(self, cognome):
        self._cognome = cognome
    # cf getter & setter
    @property
    def cf(self):
        return self._cf
    
    @cf.setter
    def cf(self, cf):
        self._cf = cf
    # iban getter & setter
    @property
    def iban(self):
        return self._iban
    
    @iban.setter
    def iban(self, iban):
        self._iban = iban
    # id_tipo_contratto getter & setter
    @property
    def id_tipo_contratto(self):
        return self._id_tipo_contratto
    
    @id_tipo_contratto.setter
    def id_tipo_contratto(self, id_tipo_contratto):
        self._id_tipo_contratto = id_tipo_contratto
    # email getter & setter
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email
    # telefono getter & setter
    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono
    # data_nascita getter & setter
    @property
    def data_nascita(self):
        return self._data_nascita
    
    @data_nascita.setter
    def data_nascita(self, data_nascita):
        self._data_nascita = data_nascita
    
    def __str__(self):
        return f"Id dipendente: {self._id_dipendente}, nome: {self._nome}, cognome: {self._cognome}, cf: {self._cf}, \
        iban: {self._iban}, tipo contratto: {self._id_tipo_contratto}, email: {self._email}, telefono: {self._telefono}, data di nascita: {self._data_nascita}"
        
    