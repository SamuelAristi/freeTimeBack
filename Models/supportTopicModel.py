from sqlalchemy import Column, Integer, VARCHAR
from Models.init import Base

class SupportTopic(Base):
    __tablename__ = 'SupportTopic'

    support_topic_id = Column(Integer, primary_key=True)
    support_topic_name = Column(VARCHAR(100))  

    def __repr__(self):
        return (f"<SuporTopic(suport_topic_id={self.support_topic_id}, "
        f"suport_topic_name='{self.support_topic_name}')>")
