from api.exceptions import EntityDoesNotExistException
from .models import Doctor

class DoctorRepo:

    def _decode_db_doctor(self, db_doctor):
        return Doctor(id=db_doctor.id,
                          name=db_doctor.name,
                          address=db_doctor.address,
                          phone=db_doctor.phone,
                          district=db_doctor.district,
                          fee=db_doctor.fee,
                          category=db_doctor.category)

    def get_doctor(self, id=None, free=None, district=None, category=None):
        try:
            if id is not None:
                return Doctor.objects.get(id=id)
            elif free is not None:
                return Doctor.objects.get(free=free)
            elif district is not None:
                return Doctor.objects.get(district=district)
            else:
                return Doctor.objects.get(category=category)        
        except Doctor.DoesNotExist:
            raise EntityDoesNotExistException

    def get_all_doctor(self):
        try:
            return Doctor.objects.all()
        
        except Doctor.DoesNotExist:
            raise EntityDoesNotExistException

    def create_doctor(self, doctor):
        db_doctor = Doctor.objects.create(name=doctor.name,
                                        address=doctor.address,
                                        phone=doctor.phone,
                                        district=doctor.district,
                                        fee=doctor.fee,
                                        category=doctor.category,
                                        language=doctor.language)
        return self._decode_db_doctor(db_doctor)