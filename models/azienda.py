from pydantic import BaseModel

class Azienda_model(BaseModel):
    id_azienda: str
    nome: str | None = None
    p_iva: str | None = None
    indirizzo: str | None = None
    cap: str | None = None
    iban: str | None = None
    telefono: str | None = None
    email: str | None = None
    pec: str | None = None
    fax: str | None = None