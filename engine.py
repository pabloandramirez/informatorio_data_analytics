from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine('postgresql://postgres:nolocreo@localhost/dataBase18/07')

Base = declarative_base()

class Empleado(Base):
    __tablename__ = 'empleado'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    apellido = Column(String(50))

class Pedido(Base):
    __tablename__ = 'pedido'
    id = Column(Integer, primary_key=True, autoincrement=True)
    texto = Column(String(50))
    fecha_hora = Column(DateTime)
    empleado_id = Column(Integer, ForeignKey('empleado.id'))
    empleado = relationship(Empleado)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()