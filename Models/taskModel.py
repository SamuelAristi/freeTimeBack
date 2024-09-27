from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey,DECIMAL, Time, String
from Models.init import Base

class Task(Base):
    __tablename__ = 'Task'

    task_id = Column(Integer, primary_key=True) # id de la tarea
    task_title = Column(String(100), nullable=False)  # Título de la tarea
    task_offer = Column(DECIMAL, nullable=False)  # Oferta realizada por el usuario
    task_offer_suggested = Column(DECIMAL, nullable=True)  # Oferta sugerida por la aplicación
    task_description = Column(Text, nullable=False)  # Descripción de la tarea
    task_stimed_time_hours = Column(DECIMAL, nullable=False)  # Tiempo estimado en horas
    task_type_id = Column(Integer, ForeignKey('TaskType.task_type_id'))  # Tipo de tarea
    task_execution_date = Column(DateTime, nullable=False)  # Fecha de ejecución
    task_execution_time = Column(Time, nullable=False)  # Hora de ejecución
    task_address = Column(String(255), nullable=False)  # Dirección donde debe ejecutarse la tarea

    def __repr__(self):
        return (f"<Task(task_id={self.task_id}, task_title={self.task_title}, "
                f"task_offer={self.task_offer}, task_offer_suggested={self.task_offer_suggested}, "
                f"task_description={self.task_description}, "
                f"task_stimed_time_hours={self.task_stimed_time_hours}, "
                f"task_type_id={self.task_type_id}, task_execution_date={self.task_execution_date}, "
                f"task_execution_time={self.task_execution_time}, task_address={self.task_address})>")
