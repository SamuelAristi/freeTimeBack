from sqlalchemy import Column, Text, Integer,DateTime, ForeignKey
from Models.init import Base

class Disable(Base):
    __tablename__ = 'Disable'

    disable_id = Column(Integer, primary_key=True)
    disable_user_description = Column(Text(1000), nullable=False)  # Longitud especificada
    disable_user_date= Column(DateTime, nullable=False) 
    user_id = Column(Integer, ForeignKey('User.user_id')) #llave foranea del id del usuario

    def __repr__(self):
        return (f"Disable(disable_id={self.disable_id}, disable_user_description='{self.disable_user_description}',"
                f" Disable_user_date='{self.disable_user_date}, user_id={self.user_id} )>")