from category.serializer import CatetorySerializer


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
                   'category': CatetorySerializer.serialize(doctor.category)
               }