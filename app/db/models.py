# models.py
from app.db.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
class Usuario(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, index=True)
    nombre = Column(String)
    apellido = Column(String)
    direccion = Column(String)
    telefono = Column(Integer)
    correo = Column(String)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    estado = Column(Boolean, default=True)
class Paciente(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String)
    apellido = Column(String)
    direccion = Column(String)
    telefono = Column(Integer)
    correo = Column(String)
    created_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
class Resultado(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_paciente = Column(Integer, index=True)
    id_usuario = Column(Integer, index=True)
    fecha = Column(DateTime)
    resultado = Column(String)
    created_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


