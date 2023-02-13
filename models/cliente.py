from pydantic import BaseModel, validator

class Cliente_model(BaseModel):
    id_cliente: str
    nome: str | None = None
    p_iva: str | None = None
    indirizzo: str | None = None
    cap: str | None = None
    iban: str | None = None
    telefono: str | None = None
    email: str | None = None
    pec: str | None = None
    fax: str | None = None
    
    
# validazione id_cliente
    # @validator('id_cliente')
    # def validate_id_customer(cls, v):
    #     assert len(v) <= 80, "Maximum length for 'id_cliente' is 80 characters"
    #     assert len(v) > 0, "'id_cliente' must contain at least 1 character"
    #     return v
    # # validazione nome
    # @validator('nome')
    # def validate_name(cls, v):
    #     if v:
    #         assert len(v) <= 90, "Maximum length for 'nome' is 90 characters"
    #         return v
    # # validazione p_iva
    # @validator('p_iva')
    # def validate_p_iva(cls, v):
    #     if v:
    #         assert len(v) <= 11, "Maximum length for 'p_iva' is 11 characters"
    #         return v
    # # validazione indirizzo
    # @validator('indirizzo')
    # def validate_adress(cls, v):
    #     if v:
    #         assert len(v) <= 90, "Maximum length for 'indirizzo' is 90 characters"
    #         return v
    # # validazione cap
    # @validator('cap')
    # def validate_cap(cls, v):
    #     if v:
    #         assert len(v) <= 5, "Maximum length for 'cap' is 5 characters"
    #         return v
    # # validazione iban
    # @validator('iban')
    # def validate_iban(cls, v):
    #     if v:
    #         assert len(v) <= 27, "Maximum length for 'iban' is 27 characters"
    #         return v
    # # validazione telefono
    # @validator('telefono')
    # def validate_phone(cls, v):
    #     if v:
    #         assert len(v) <= 15, "Maximum length for 'telefono' is 15 characters"
    #         return v
    # # validazione email
    # @validator('email')
    # def validate_email(cls, v):
    #     if v:
    #         assert len(v) <= 90, "Maximum length for 'email' is 90 characters"
    #         return v
    # # validazione pec
    # @validator('pec')
    # def validate_pec(cls, v):
    #     if v:
    #         assert len(v) <= 45, "Maximum length for 'pec' is 45 characters"
    #         return v
    # # validazione fax
    # @validator('fax')
    # def validate_fax(cls, v):
    #     if v:
    #         assert len(v) <= 15, "Maximum length for 'fax' is 15 characters"
    #         return v