from sqlalchemy import Column, Integer, SmallInteger, Text, ForeignKey
from Models.init import Base

class UserReview(Base):
    __tablename__ = 'UserReview'

    user_review_id = Column(Integer, primary_key=True, autoincrement=True)
    user_review_calification = Column(SmallInteger, nullable=False)  # Calificación del usuario, con rango de SMALLINT
    user_review_description = Column(Text, nullable=True)  # Descripción de la reseña, tipo TEXT
    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)  # Relación con la tabla 'User'

    def __repr__(self):
        return (f"<UserReview(user_review_id={self.user_review_id}, user_review_calification={self.user_review_calification}, "
                f"user_review_description='{self.user_review_description}', user_id={self.user_id})>")
