from pydantic import BaseModel, validator 
import datetime
from typing import Optional

class Dipendente_model(BaseModel):
    id_dipendente: str
    nome: Optional[str]= ''
    cognome: Optional[str]= ''
    cf: str 
    iban: str 
    id_tipo_contratto: str 
    email: Optional[str]= ''
    telefono: Optional[str]= ''
    data_nascita: Optional[datetime.date]= ''

    # # validazione id_dipendente
    # @validator('id_dipendente')
    # def validate_id_dipendente(cls, v):
    #     assert len(v) <= 80, "maximum length for 'id_dipendente' is 80 characters"
    #     assert len(v) > 0, "'id_dipendente' must contain at least 1 character"
    #     return v
    # # validazione nome
    # @validator('nome')
    # def validate_name(cls, v):
    #     if v:
    #         assert len(v) <= 45, "maximum length for 'nome' is 45 characters"
    #         return v
    # # validazione cognome
    # @validator('cognome')
    # def validate_lastname(cls, v):
    #     if v:
    #         assert len(v) <= 45, "maximum length for 'cognome' is 45 characters"
    #         return v
    # # validazione cf
    # @validator('cf')
    # def validate_fc(cls, v):
    #     assert len(v) <= 16, "maximum length for 'cf' is 16 characters"
    #     assert len(v) > 0, "'cf' must contain at least 1 character"
    #     return v
    # # validazione iban
    # @validator('iban')
    # def validate_iban(cls, v):
    #     assert len(v) <= 16, "maximum length for 'iban' is 45 characters"
    #     assert len(v) > 0, "'iban' must contain at least 1 character"
    #     return v
    # # validazione id_tipo_contratto
    # @validator('id_tipo_contratto')
    # def validate_type_contract(cls, v):
    #     assert len(v) <= 80, "maximum length for 'id_tipo_contratto' is 80 characters"
    #     assert len(v) > 0, "'id_tipo_contratto' must contain at least 1 character"
    #     return v
    # # validazione email
    # @validator('email')
    # def validate_email(cls, v):
    #     if v:
    #         assert len(v) <= 90, "maximum length for 'email' is 90 characters"
    #         return v
    # # validazione telefono
    # @validator('telefono')
    # def validate_phone(cls, v):
    #     if v:
    #         assert len(v) <= 45, "maximum length for 'telefono' is 45 characters"
    #         return v
    
    

    