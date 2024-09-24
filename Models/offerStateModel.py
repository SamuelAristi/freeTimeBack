from sqlalchemy import Column, Integer, String,VARCHAR
from Models.init import Base

class OfferState(Base):
    __tablename__ = 'OfferState'

    offer_state_id = Column(Integer, primary_key=True)
    offer_state_name = Column(VARCHAR(40),nullable=False)  

    def __repr__(self):
        return (f"<OfferState(offer_state_id={self.offer_state_id}, "
        f"offer_state_name='{self.offer_state_name}')>")