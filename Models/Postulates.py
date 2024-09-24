from sqlalchemy import Column, Integer, ForeignKey,DECIMAL,DateTime
from Models.init import Base

class Postulates(Base):
    __tablename__ = 'Postulates'

    postulate_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id_freetimer = Column(Integer, ForeignKey('User.user_id'),nullable=False)  # ID del rol (llave foránea)
    offer_id = Column(Integer,ForeignKey('Offer.offer_id'),nullable=False)  # ID de la oferta (llave foránea)
    postulate_price = Column(DECIMAL, nullable= True)
    postulate_date = Column(DateTime, nullable= True)

    def __repr__(self):
        return (f"<Postulates(postulate_id={self.postulate_id}, user_id_freetimer={self.user_id_freetimer},"
                f"offer_id={self.offer_id}, postulate_price={self.postulate_price}, postulate_date={self.postulate_date})>")