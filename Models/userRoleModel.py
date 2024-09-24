from sqlalchemy import Column, Integer, ForeignKey
from Models.init import Base

class UsersRole(Base):
    __tablename__ = 'UsersRole'

    user_role_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.user_id'),nullable=False)  
    role_id = Column(Integer,ForeignKey('Role.role_id'),nullable=False)  

    def __repr__(self):
        return f"<UsersRole(user_role_id={self.user_role_id}, user_id={self.user_id}, role_id={self.role_id})>"