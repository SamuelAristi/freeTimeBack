from sqlalchemy import Column, Integer,ForeignKey, VARCHAR
from Models.init import Base

class Account(Base):
    __tablename__ = 'Account'

    account_id = Column(Integer, primary_key=True)
    account_number = Column(VARCHAR(30), unique= True,nullable=False)
    bank_id = Column(Integer, ForeignKey('Bank.bank_id'),nullable=False)
    account_Type_id = Column(Integer, ForeignKey('AccountType.account_Type_id'),nullable=False)
    user_id = Column(Integer, ForeignKey('User.user_id'),nullable=False)  # ID del rol (llave foránea)

    def __repr__(self):
        return (f"<Account(account_id={self.account_id}, "
        f"account_number={self.account_number}, " 
        f"bank_id={self.bank_id}, "
        f"account_Type_id={self.account_Type_id}, user_id={self.user_id})>")
