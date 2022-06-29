from doctor.serializers import DoctorSerializer, MultipleDoctorsSerializer


class DoctorView:

    def __init__(self, get_all_doctors_interactor=None, create_new_doctor_interactor=None):
        self.get_all_doctors_interactor = get_all_doctors_interactor
        self.create_new_doctor_interactor = create_new_doctor_interactor

    def get(self, district=None, category=None, price_range=None, language= None):
        doctors = self.get_all_doctors_interactor.set_params(district=district, category=category,
                                                                     price_range=price_range, language=language).execute()

        body = MultipleDoctorsSerializer.serialize(doctors)
        status = 200
        return body, status

    def post(self, name=None, address=None, fee=None, phone=None, category=None, district=None):
        doctor = self.create_new_doctor_interactor \
                .set_params(name=name, address=address, fee=fee, \
                        phone=phone, category=category, district=district).execute()
        body = DoctorSerializer.serialize(doctor)
        status = 201
        return body, status