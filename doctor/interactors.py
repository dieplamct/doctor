import json
from doctor.models import Doctor
from schedule.models import Schedule

class GetDoctorInteractor:
    def __init__(self, doctor_repo):
        self.doctor_repo = doctor_repo

    def set_params(self, id, district, category, fee, language):
        self.id = id
        self.fee = fee
        self.language = language
        self.district = district
        self.category = category
        return self
    
    def get_doctor(self):
        return self.doctor_repo.get_doctor(self.id,
                                            self.fee,
                                            self.district,
                                            self.category,                                            
                                            self.language)

    def get_all_doctor(self):
        return self.doctor_repo.get_all_doctor()

class CreateNewDoctorInteractor:
    def __init__(self, doctor_repo, category_repo, district_repo, schedule_repo, language_repo):
        self.doctor_repo = doctor_repo
        self.category_repo = category_repo
        self.district_repo = district_repo
        self.schedule_repo = schedule_repo
        self.language_repo = language_repo

    def set_params(self, name, address, phone, fee, category, district, schedule, language):
        self.name = name
        self.address = address
        self.district = district
        self.category = category
        self.phone = phone
        self.fee = fee
        self.schedule = schedule
        self.language = language
        return self
    
    def execute(self):
        category_instance = self.category_repo.get_category(self.category)
        district_instance = self.district_repo.get_distict(self.district)
        language_instance = self.language_repo.get_language(self.language)
        doctor = Doctor(name=self.name, address=self.address, phone=self.phone, \
                        fee=self.fee, category=category_instance, district=district_instance, language=language_instance)
        doctor_result = self.doctor_repo.create_doctor(doctor)
        schedule = Schedule(mon = self.schedule.get('mon'), \
                            tue = self.schedule.get('tue'), \
                            wend = self.schedule.get('wend'), \
                            thur = self.schedule.get('thur'), \
                            frid = self.schedule.get('frid'), \
                            satu = self.schedule.get('satu'), \
                            sun = self.schedule.get('sun'), \
                            doctor = doctor_result, \
                            language=language_instance)
        self.schedule_repo.create_schedule(schedule)
        doctor_result.language = language_instance
        return doctor_result
        