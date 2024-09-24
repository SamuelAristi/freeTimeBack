from sqlalchemy import Column, Integer, VARCHAR
from Models.init import Base

class Role(Base):
    __tablename__ = 'Role'

    role_id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(VARCHAR(50), nullable=False)  # Nombre del rol con longitud especificada

    def __repr__(self):
        return (f"<Role(role_id={self.role_id}, role_name='{self.role_name}')>")