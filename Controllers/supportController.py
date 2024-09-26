from Models.supportModel import Support
from Models.userModel import User  
from sync import Session  
from datetime import datetime

# Función para crear un soporte
def create_support(support_description, user_id, support_state_id):
    try:
        session = Session()  # Inicia la sesión
        
        new_support = Support(
            support_date=datetime.now(),
            support_description=support_description,
            user_id=user_id,
            support_state_id=support_state_id
        )
        
        session.add(new_support)  
        session.commit()  
        return new_support
    except Exception as e:
        print(f"Error al crear soporte: {str(e)}")
        return None
    finally:
        session.close()  

# Función para listar todos los soportes junto con los datos del usuario
def get_supports():
    try:
        session = Session()  # Inicia la sesión
        
        # Realiza un join entre Support y User
        supports = session.query(Support, User).join(User, Support.user_id == User.user_id).all()
        
        # Crea la lista con los soportes y la información del usuario
        support_list = [{
            "support_id": s.Support.support_id, 
            "support_description": s.Support.support_description,
            "support_date": s.Support.support_date,
            "user_id": s.Support.user_id,
            "support_state_id": s.Support.support_state_id,
            "user_name": s.User.user_full_name,  
            "user_email": s.User.user_email 
        } for s in supports]
        
        return support_list
    except Exception as e:
        print(f"Error al listar soportes: {str(e)}")
        return None
    finally:
        session.close()  
