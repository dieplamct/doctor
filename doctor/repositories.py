from api.exceptions import EntityDoesNotExistException
from .models import Doctor

class DoctorRepo:

    def get_doctor(self, id=None, free=None, district=None):
        try:
            pass
        
        except Doctor.DoesNotExist:
            raise EntityDoesNotExistException