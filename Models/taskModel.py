from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey,DECIMAL, VARCHAR
from Models.init import Base

class Task(Base):
    __tablename__ = 'Task'

    task_id = Column(Integer, primary_key=True)
    task_title = Column(VARCHAR(255), nullable= False)
    task_offer_suggested = Column(DECIMAL)
    task_description = Column(Text(400))
    task_stimed_time_hours = Column(DECIMAL, nullable= False)
    task_name = Column(VARCHAR(100), nullable= False)
    task_address = Column(VARCHAR(100), nullable = False)
    task_type_id = Column(Integer, ForeignKey('TaskType.task_type_id'),nullable=False)

    def __repr__(self):
        return (f"<Task(task_id={self.task_id}, "
                f"task_title={self.task_title}, "
                f"task_offer_suggested={self.task_offer_suggested}, "
                f"task_description={self.task_description}, "
                f"task_stimed_time_hours={self.task_stimed_time_hours}, "
                f"task_name={self.task_name},"
                f"task_address={self.task_name},"
                f"task_type_id={self.task_type_id})>")
