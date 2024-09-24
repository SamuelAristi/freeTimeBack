from sqlalchemy import Column, Integer, VARCHAR
from Models.init import Base

class AccountType(Base):
    __tablename__ = 'AccountType'

    account_Type_id = Column(Integer, primary_key=True,nullable=False)
    account_Type_name = Column(VARCHAR(20),nullable=False)  

    def __repr__(self):
        return (f"<AccountType(account_Type_id={self.account_Type_id}, "
        f"account_Type_name='{self.account_Type_name}')>")
