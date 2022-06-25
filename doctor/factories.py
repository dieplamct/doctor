
from doctor.interactors import CreateNewDoctorInteractor, GetAllDoctorInteractor
from doctor.repositories import DoctorRepo
from doctor.views import DoctorView


def create_doctor_repo():
    return DoctorRepo()

def create_create_new_doctor():
    return CreateNewDoctorInteractor(create_doctor_repo())

def create_doctor_view(request, **kwargs):
    return DoctorView(get_all_doctors_interactor=GetAllDoctorInteractor(doctor_repo=create_doctor_repo()))