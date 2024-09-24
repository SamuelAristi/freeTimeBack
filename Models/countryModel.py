from sqlalchemy import Column, VARCHAR, Integer, Boolean, BLOB
from Models.init import Base

class Country(Base):
    __tablename__ = 'Country'

    country_id = Column(Integer, primary_key=True)
    country_name = Column(VARCHAR(40), nullable=False)  # Longitud especificada


    def __repr__(self):
        return (f"Country(Country_id={self.country_id}, country_name='{self.country_name}' )>")