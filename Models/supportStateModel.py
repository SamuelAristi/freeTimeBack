from sqlalchemy import Column, Integer, VARCHAR
from Models.init import Base

class SupportState(Base):
    __tablename__ = 'SupportState'

    support_state_id = Column(Integer, primary_key=True)
    support_state_name = Column(VARCHAR(100))  # Asumiendo que el límite es 50 caracteres

    def __repr__(self):
        return (f"<SuporState(suport_state_id={self.support_state_id}, "
        f"suport_state_name='{self.support_state_name}')>")
