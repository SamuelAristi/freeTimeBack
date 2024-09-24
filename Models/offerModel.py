from sqlalchemy import Column, Integer, DateTime, ForeignKey,VARCHAR,DECIMAL
from Models.init import Base

class Offer(Base):
    __tablename__ = 'Offer'

    offer_id = Column(Integer, primary_key=True)
    offer_date = Column(DateTime)
    offer_inicial_price = Column(DECIMAL)
    address = Column(VARCHAR(150))
    offer_freetimer_calification = Column(Integer)
    offer_fulltimer_calification = Column(Integer)
    task_id = Column(Integer, ForeignKey('Task.task_id'))
    user_id_fulltimer = Column(Integer, ForeignKey('User.user_id'))
    offer_start_date = Column(DateTime)
    offer_end_date = Column(DateTime)
    offer_state_id = Column(Integer, ForeignKey('OfferState.offer_state_id'))
    user_id_freetimer = Column(Integer)
    offer_final_price = Column(DECIMAL)
    
    def __repr__(self):
        return (f"<Offer(offer_id={self.offer_id}, "
                f"offer_date={self.offer_date}, "
                f"offer_inicial_price ={self.offer_inicial_price}, "
                f"address ={self.address}, "
                f"offer_freetimer_calification={self.offer_freetimer_calification}, "
                f"offer_fulltimer_calification={self.offer_fulltimer_calification}"
                f"task_id={self.task_id}"
                f"user_id_fulltimer={self.user_id_fulltimer}"
                f"offer_start_date={self.offer_start_date}"
                f"offer_end_date={self.offer_end_date}"
                f"offer_state_id={self.offer_state_id}"
                f"user_id_freetimer={self.user_id_freetimer}"
                f"offer_final_price ={self.offer_final_price} )>")