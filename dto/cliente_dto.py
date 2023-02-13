class Cliente:
    def __init__(self, id_cliente, nome, p_iva, indirizzo, cap, iban, telefono, email, pec, fax):
        self.id_cliente = id_cliente
        self.nome = nome
        self.p_iva = p_iva
        self.indirizzo = indirizzo
        self.cap = cap
        self.iban = iban
        self.telefono = telefono
        self.email = email
        self.pec = pec
        self.fax = fax
        
     # id_cliente getter & setter
    @property
    def id_cliente(self):
        return self._id_cliente
    
    @id_cliente.setter    
    def id_cliente(self, id_cliente):
        self._id_cliente = id_cliente
    # nome getter & setter   
    @property
    def nome(self):
        return self._nome
    
    @nome.setter    
    def nome(self, nome):
        self._nome = nome
    # p_iva getter & setter
    @property
    def p_iva(self):
        return self._p_iva 
    
    @p_iva.setter    
    def p_iva(self, p_iva):
        self._p_iva = p_iva
    # indirizzo getter & setter
    @property
    def indirizzo(self):
        return self._indirizzo 
    
    @indirizzo.setter    
    def indirizzo(self, indirizzo):
        self._indirizzo = indirizzo
    # cap getter & setter
    @property
    def cap(self):
        return self._cap 
    
    @cap.setter    
    def cap(self, cap):
        self._cap = cap
    # iban getter & state
    @property
    def iban(self):
        return self._iban 
    
    @iban.setter    
    def iban(self, iban):
        self._iban = iban
    # telefono getter & setter
    @property
    def telefono(self):
        return self._telefono 
    
    @telefono.setter    
    def telefono(self, telefono):
        self._telefono = telefono
    # email getter & setter
    @property
    def email(self):
        return self._email 
    
    @email.setter    
    def email(self, email):
        self._email = email
    # pec getter & setter
    @property
    def pec(self):
        return self._pec 
    
    @pec.setter    
    def pec(self, pec):
        self._pec = pec
    # fax getter & setter
    @property
    def fax(self):
        return self._fax 
    
    @fax.setter    
    def fax(self, fax):
        self._fax = fax
    
    
    def __str__(self):
        return f"Id cliente: {self._id_cliente}, nome: {self._nome}, partita IVA: {self._p_iva},indirizzo : {self.indirizzo}, cap: {self._cap}, iban: {self._iban} telefono: {self._telefono}, email: {self._email}, pec: {self._pec}, fax: {self._fax}"