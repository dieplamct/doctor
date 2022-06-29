from doctor.models import Doctor
from doctor.serializers import DoctorSerializer, MultipleDoctorsSerializer


class DoctorView:

    def __init__(self, get_doctor_interactor=None, create_new_doctor_interactor=None):
        self.get_doctor_interactor = get_doctor_interactor
        self.create_new_doctor_interactor = create_new_doctor_interactor
    
    def __get_all_doctor(self) :
        doctors = self.get_doctor_interactor.get_all_doctor()
        body = MultipleDoctorsSerializer.serialize(doctors)
        return body

    def get(self, id = None, district=None, category=None, fee=None, language= None):
        if id is not None or district is not None or fee is not None or language is not None or category is not None:
            doctor = self.get_doctor_interactor.set_params(id = id,
                                                            district=district,
                                                            category=category,
                                                            fee=fee,
                                                            language=language).get_doctor()
            if isinstance(doctor, Doctor):
                body = DoctorSerializer.serialize(doctor)
            else:
                body = MultipleDoctorsSerializer.serialize(doctor)
                
        else:
            body = self.__get_all_doctor()
        
        status = 200
        return body, status

    def post(self, name=None, address=None, fee=None, phone=None, category=None, district=None, schedule=None, language=None):
        doctor = self.create_new_doctor_interactor \
                .set_params(name=name, address=address, fee=fee, \
                        phone=phone, category=category, district=district, \
                        schedule=schedule, language=language).execute()
        body = DoctorSerializer.serialize(doctor)
        status = 201
        return body, status