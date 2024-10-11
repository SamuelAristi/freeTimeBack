#Importacion de librerias 
from sqlalchemy import Column, VARCHAR, Integer,ForeignKey
from Models.init import Base

class City(Base):
    __tablename__ = 'City'

    #Modelo para la tabla city, y tener igualdad con la base de datos
    city_id = Column(Integer, primary_key=True)
    city_name = Column(VARCHAR(70), nullable=False)  #
    state_id = Column(Integer, ForeignKey('State.state_id'), nullable=False) 

    #Devuelve una cadena con la instacion de la tabla city, mostrando los valores y los atributos
    def __repr__(self):
        return (f"City(City_id={self.city_id}, city_name='{self.city_name}, state_id={self.state_id}' )>")