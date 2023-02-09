from token import OP
from pydantic import BaseModel, validator 
import datetime
from typing import Optional

class Dipendente_azienda(BaseModel):
    id_dipendente: str
    id_azienda: str
    data_inizio: datetime.date
    matricola: Optional[str]=''
    data_fine: Optional[datetime.date]=''