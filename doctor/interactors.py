from doctor.models import Doctor


class GetAllDoctorInteractor:
    def __init__(self, doctor_repo):
        self.doctor_repo = doctor_repo

    def set_params(self, district, category, price_range, language):
        self.price_range = price_range
        self.language = language
        self.district = district
        self.category = category
        return self
    
    def execute(self):
        return self.doctor_repo.get_all_doctor()

class CreateNewDoctorInteractor:
    def __init__(self, doctor_repo):
        self.doctor_repo = doctor_repo

    def set_params(self, district, category, price_range, language):
        self.price_range = price_range
        self.language = language
        self.district = district
        self.category = category
        return self
    
    def execute(self):
        doctor = Doctor(title=self.title, description=self.description, author_id=self.logged_person_id)
        return self.doctor_repo.create_doctor(doctor)