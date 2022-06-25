from category.serializer import CatetorySerializer


class MultipleDoctorsSerializer:

    @staticmethod
    def  serialize(experiences):
        return [DoctorSerializer.serialize(experience) for experience in experiences]


class DoctorSerializer:

    @staticmethod
    def serialize(doctor):
        return {
                   'id': str(doctor.id),
                   'name': doctor.name,
                   'address': doctor.address,
                   'phone': doctor.picture,
                   'fee': doctor.fee,
                   'category': CatetorySerializer.serialize(doctor.category)
               }