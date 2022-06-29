
from category.repositories import CategoryRepo, CategoryTranslatorRepo
from district.repositories import DistrictRepo
from doctor.interactors import CreateNewDoctorInteractor, GetAllDoctorInteractor
from doctor.repositories import DoctorRepo
from doctor.views import DoctorView


def create_doctor_repo():
    return DoctorRepo()

def create_category_repo():
    return CategoryRepo()

def create_category_translator_repo():
    return CategoryTranslatorRepo()

def create_district_repo():
    return DistrictRepo()

def create_new_doctor():
    return CreateNewDoctorInteractor(doctor_repo=create_doctor_repo(), category_repo=create_category_repo(), district_repo=create_district_repo())

def create_get_all_doctor():
    return GetAllDoctorInteractor(doctor_repo=create_doctor_repo())

def create_doctor_view(request, **kwargs):
    return DoctorView(get_all_doctors_interactor=create_get_all_doctor(), create_new_doctor_interactor=create_new_doctor())