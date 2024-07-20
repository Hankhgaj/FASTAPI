from fastapi import APIRouter,Depends,status 
from app.schemas import Usuario,MostarUsuario,ActualizarUsuario
from app.db.database import get_db
from sqlalchemy.orm import Session 
from typing import List
from app.repository import user 
from app.oauth import get_current_user
router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

@router.get('/',response_model=List[MostarUsuario],status_code=status.HTTP_200_OK)
def obtener_usuarios(db:Session = Depends(get_db),current_user: Usuario = Depends(get_current_user)):
    data = user.obtener_usuarios(db)
    return data

@router.post('/',status_code=status.HTTP_201_CREATED)
def crear_usuario(usuario:Usuario,db:Session = Depends(get_db)):
    user.crear_usuario(usuario,db)
    return {"respuesta":"Usuario creado satisfactoriamente!!"}

@router.get('/{user_id}',response_model=MostarUsuario,status_code=status.HTTP_200_OK)
def obtener_usuario(user_id:int,db:Session = Depends(get_db)):
    usuario = user.obtener_usuario(user_id,db)
    return usuario

@router.delete('/{user_id}',status_code=status.HTTP_200_OK)
def eliminar_usuario(user_id:int,db:Session = Depends(get_db)):
    res = user.eliminar_usuario(user_id, db)
    return res 

@router.patch('/{user_id}',status_code=status.HTTP_200_OK)
def actualizar_usuario(user_id:int,updateUser:ActualizarUsuario,db:Session = Depends(get_db)):
    res = user.actualizar_user(user_id,updateUser, db)
    return res 