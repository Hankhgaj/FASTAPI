
from pydantic import BaseModel
from typing import Optional, Union
from datetime import datetime
#User Model
class Usuario(BaseModel):
    username:str
    password:str
    nombre:str
    apellido:str
    direccion:Optional[str]
    telefono:int
    correo:str
    created_at:datetime =datetime.now()

class AgregarUsuario(BaseModel):
    username:str
    password:str
    nombre:str
    apellido:str
    direccion:Optional[str]
    telefono:int
    correo:str
class ActualizarUsuario(BaseModel):
    username:str
    password:str
    nombre:str
    apellido:str
    direccion:Optional[str]
    telefono:int
    correo:str
class MostarUsuario(BaseModel):
    username:str 
    nombre:str 
    correo:str 
    class Config():
        from_attributes = True 
class Login(BaseModel):
    username:str
    password:str
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None
