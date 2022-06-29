from category.serializer import CatetorySerializer
from district.serializer import DistrictSerializer
from language.serializer import LanguageSerializer


class MultipleDoctorsSerializer:

    @staticmethod
    def serialize(doctors):
        return [DoctorSerializer.serialize(doctor) for doctor in doctors]


class DoctorSerializer:

    @staticmethod
    def serialize(doctor):
        return {
                   'id': str(doctor.id),
                   'name': doctor.name,
                   'address': doctor.address,
                   'phone': doctor.phone,
                   'fee': str(doctor.fee),
                   'district': DistrictSerializer.serialize(doctor.district),
                   'category': CatetorySerializer.serialize(doctor.category),
                   'language': LanguageSerializer.serialize(doctor.language)
               }