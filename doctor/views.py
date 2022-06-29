from doctor.serializers import DoctorSerializer, MultipleDoctorsSerializer


class DoctorsView:

    def __init__(self, get_all_doctors_interactor=None, create_new_doctor_interactor=None):
        self.get_all_doctors_interactor = get_all_doctors_interactor
        self.create_new_doctor_interactor = create_new_doctor_interactor

    def get(self, id = None, district=None, category=None, price_range=None, language= None):
        doctors = self.get_all_doctors_interactor.set_params(id = id, district=district, category=category,
                                                                     price_range=price_range, language=language).execute()
        body = MultipleDoctorsSerializer.serialize(doctors)
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


class DoctorView:

    def __init__(self, get_doctor_interactor=None):
        self.get_doctor_interactor = get_doctor_interactor

    def get(self, id = None):
        doctor = self.get_doctor_interactor.set_params(id = id).execute()
        body = DoctorSerializer.serialize(doctor)
        status = 200
        return body, status