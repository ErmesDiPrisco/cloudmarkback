from unittest.mock import patch
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import router.azienda as azienda
import router.dipendente as dipendente
import router.cliente as cliente

app=FastAPI()

origins = [
    'http://localhost:4200',
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods= ['*'],
    allow_headers=["*"],
)

app.include_router(azienda.router)
app.include_router(dipendente.router)
app.include_router(cliente.router)

