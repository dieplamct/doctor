
from category.repositories import CategoryRepo, CategoryTranslatorRepo
from district.repositories import DistrictRepo
from doctor.interactors import CreateNewDoctorInteractor, GetAllDoctorInteractor, GetDoctorInteractor
from doctor.repositories import DoctorRepo
from doctor.views import DoctorView, DoctorsView
from language.repositories import LanguageRepo
from schedule.repositories import ScheduleRepo


def create_doctor_repo():
    return DoctorRepo()

def create_category_repo():
    return CategoryRepo()

def create_category_translator_repo():
    return CategoryTranslatorRepo()

def create_district_repo():
    return DistrictRepo()

def create_schedule_repo():
    return ScheduleRepo()

def create_language_repo():
    return LanguageRepo()

def create_new_doctor():
    return CreateNewDoctorInteractor(doctor_repo=create_doctor_repo(), \
                                    category_repo=create_category_repo(), \
                                    district_repo=create_district_repo(), \
                                    schedule_repo=create_schedule_repo(),
                                    language_repo=create_language_repo())

def create_get_all_doctor():
    return GetAllDoctorInteractor(doctor_repo=create_doctor_repo())

def create_get_doctor():
    return GetDoctorInteractor(doctor_repo=create_doctor_repo())

def create_doctors_view(request, **kwargs):
    return DoctorsView(get_all_doctors_interactor=create_get_all_doctor(), create_new_doctor_interactor=create_new_doctor())

def create_doctor_view(request, **kwargs):
    return DoctorView(get_doctor_interactor=create_get_doctor())