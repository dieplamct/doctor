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

    def post(self, title=None, description=None, logged_person_id=None):
        doctor = self.create_new_doctor_interactor \
                .set_params(title=title, description=description, logged_person_id=logged_person_id).execute()
        body = DoctorSerializer.serialize(doctor)
        status = 201
        return body, status