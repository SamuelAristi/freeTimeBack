from sqlalchemy import Column, Integer, DateTime, Text,ForeignKey
from Models.init import Base

class Support(Base):
    __tablename__ = 'Support'

    support_id = Column(Integer, primary_key=True)
    support_date = Column(DateTime)
    support_description = Column(Text(2000))
    user_id = Column(Integer,ForeignKey('User.user_id'))
    support_state_id = Column(Integer,ForeignKey('SupportState.support_state_id'),nullable=False)

    def __repr__(self):
        return (f"<Support(support_id={self.support_id}, " 
        f"support_date={self.support_date}, "
        f"support_description='{self.support_description}', "
        f"user_id={self.user_id}, support_state_id={self.support_state_id})>")
