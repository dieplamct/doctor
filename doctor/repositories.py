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
                          category=db_doctor.category,
                          language=db_doctor.language)

    def get_doctor(self, id=None, fee=None, district=None, category=None, language=None):
        try:
            if id is not None:
                return self._decode_db_doctor(Doctor.objects.get(id=id))
            elif fee is not None:
                return Doctor.objects.filter(fee=fee)
            elif district is not None:
                return Doctor.objects.filter(district_id=district)
            elif language is not None:
                return Doctor.objects.filter(language_id=language)
            elif category is not None:
                return Doctor.objects.filter(category_id=category)
            else:
                return self._decode_db_doctor(Doctor.objects.first())
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