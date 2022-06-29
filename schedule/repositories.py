from api.exceptions import EntityDoesNotExistException
from .models import Doctor, Schedule

class ScheduleRepo:

    def _decode_db_schedule(self, db_schedule):
        return Schedule(id=db_schedule.id,
                          mon = db_schedule.mon,
                            tue = db_schedule.tue,
                            wend = db_schedule.wend,
                            thur = db_schedule.thur,
                            frid = db_schedule.frid,
                            satu = db_schedule.satu,
                            sun = db_schedule.sun,
                            doctor = db_schedule.doctor,
                            language = db_schedule.language)

    def get_schedule(self, doctor_id=None):
        try:
            return Schedule.objects.get(doctor=doctor_id)        
        except Schedule.DoesNotExist:
            raise EntityDoesNotExistException

    def create_schedule(self, schedule):
        db_schedule = Schedule.objects.create(mon = schedule.mon,
                                            tue = schedule.tue,
                                            wend =schedule.wend,
                                            thur =schedule.thur,
                                            frid =schedule.frid,
                                            satu =schedule.satu,
                                            sun = schedule.sun,
                                            doctor = schedule.doctor,
                                            language = schedule.language)
        return self._decode_db_schedule(db_schedule)