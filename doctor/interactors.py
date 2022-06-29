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
    def __init__(self, doctor_repo, category_repo, district_repo):
        self.doctor_repo = doctor_repo
        self.category_repo = category_repo
        self.district_repo = district_repo

    def set_params(self, name, address, phone, fee, category, district):
        self.name = name
        self.address = address
        self.district = district
        self.category = category
        self.phone = phone
        self.fee = fee
        return self
    
    def execute(self):
        category_instance = self.category_repo.get_category(self.category)
        district_instance = self.district_repo.get_distict(self.district)

        doctor = Doctor(name=self.name, address=self.address, phone=self.phone, \
                        fee=self.fee, category=category_instance, district=district_instance)
        return self.doctor_repo.create_doctor(doctor)