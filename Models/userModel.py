from sqlalchemy import Column, VARCHAR, Integer, Boolean, BLOB, ForeignKey, VARCHAR
from Models.init import Base

class User(Base):
    __tablename__ = 'User'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_full_name = Column(VARCHAR(70), nullable=False)  # Longitud especificada
    user_address = Column(VARCHAR(50), nullable=True)  # Longitud especificada
    user_email = Column(VARCHAR(50), unique=True, nullable=False)  # Longitud especificada y único
    user_nickname = Column(VARCHAR(20), nullable=True)  # Longitud especificada
    user_document = Column(VARCHAR(10), unique=True, nullable=False)  # Longitud especificada y único
    user_password = Column(VARCHAR(256), nullable=False)  # Longitud especificada para la contraseña
    user_photo = Column(VARCHAR(256), nullable=True)  # BLOB para almacenar fotos
    user_enable = Column(Boolean, default=False)  # TINYINT puede ser mapeado como Boolean en SQLAlchemy
    user_points = Column(Integer, default=0)  # Puntos del usuario
    user_phone_number = Column(VARCHAR(15), nullable=True)  # Número de teléfono
    city_id = Column(Integer, ForeignKey('City.city_id'),nullable=False)  # Campo para relación futura con tabla City

    def __repr__(self):
        return (f"<User(user_id={self.user_id}, user_full_name='{self.user_full_name}',user_addres={self.user_address} "
                f"user_email='{self.user_email}', user_nickname='{self.user_nickname}', "
                f"user_document='{self.user_document}',user_password={self.user_password},user_photo={self.user_photo},user_enable={self.user_enable}, "
                f"user_points={self.user_points}, user_phone_number={self.user_phone_number},city_id={self.city_id}>")