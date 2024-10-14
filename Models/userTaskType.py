from sqlalchemy import Column, Integer, ForeignKey
from Models.init import Base

class UserTaskType(Base):
    __tablename__ = 'UserTaskType'

    user_task_type = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.user_id'),nullable=False)
    task_type_id = Column(Integer, ForeignKey('TaskType.task_type_id'),nullable=False)  

    def __repr__(self):
        return (f"<UserTaskType(user_task_type={self.task_type_id},user_id={self.user_id}, task_type_id='{self.task_type_id}')>")