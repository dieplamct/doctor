from mock import Mock

from doctor.models import Doctor
from doctor.serializers import DoctorSerializer
from doctor.views import DoctorView

class TestDoctorView:

    def test_post_returns_doctor_serialized_and_200(self):
        TestDoctorView._ScenarioMaker() \
                .given_an_interactor_that_returns_that_doctor() \
                .given_an_id() \
                .when_post_is_called() \
                .then_interactor_receives_params() \
                .then_response_status_is_200() \
                .then_response_body_is_doctor_serialized()

    class _ScenarioMaker:

        def __init__(self):
            self._interactor_mock = Mock()
            self._interactor_mock.set_params.return_value = self._interactor_mock
            self._doctor = None
            self._id = None
            self._name = None
            self._address = None
            self._fee = None
            self._phone = None
            self._category = None
            self._distict = None
            self._schedule = None
            self._language = None

        def given_a_doctor(self):
            self._doctor = Doctor(id='1', name='unit', address='python', district='1', fee='15', category='3')
            return self

        def given_an_interactor_that_returns_that_doctor(self):
            self._interactor_mock.get_doctor.return_value = self._doctor
            return self

        def given_an_id(self):
            self._id = '2'
            return self

        def when_post_is_called(self):
            view = DoctorView(get_doctor_interactor=self._interactor_mock, create_new_doctor_interactor=self._interactor_mock)
            self._body, self._status = view.post(name=None, address=None, fee=None, phone=None, category=None, district=None, schedule=None, language=None)
            return self

        def then_interactor_receives_params(self):
            self._interactor_mock.set_params.assert_called_once_with(doctor_id=self._id)
            return self

        def then_response_status_is_200(self):
            assert self._status == 200
            return self

        def then_response_body_is_doctor_serialized(self):
            assert self._body == DoctorSerializer.serialize(self._doctor)