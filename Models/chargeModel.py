from sqlalchemy import Column, Integer, DateTime, DECIMAL, ForeignKey,VARCHAR
from Models.init import Base

class Charge(Base):
    __tablename__ = 'Charge'

    charge_id = Column(Integer, primary_key=True, autoincrement=True)
    charge_date = Column(DateTime, nullable=False)  # Fecha y hora de la carga
    charge_value = Column(DECIMAL, nullable=False)  # Valor de la carga
    charge_reference = Column(VARCHAR(40), nullable=False)  # Referencia de la carga con longitud especificada
    account_id = Column(Integer, ForeignKey('Account.account_id'),nullable=False)

    def __repr__(self):
        return (f"<Charge(charge_id={self.charge_id}, charge_date='{self.charge_date}', "
                f"charge_value={self.charge_value}, "
                f"charge_reference='{self.charge_reference}', account_id={self.account_id})>")