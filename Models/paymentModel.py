from sqlalchemy import Column, Integer, DateTime, ForeignKey, DECIMAL
from Models.init import Base

class Payment(Base):
    __tablename__ = 'Payment'

    payment_id = Column(Integer, primary_key=True)
    payment_date = Column(DateTime)
    payment_value = Column(DECIMAL)
    offer_id = Column(Integer,ForeignKey('Offer.offer_id'))

    def __repr__(self):
        return (f"<Offer(payment_id={self.payment_id}, "
                f"payment_date={self.payment_date}, "
                f"payment_value={self.payment_value}, "
                f"offer_id={self.offer_id})>")