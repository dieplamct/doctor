
class SheduleSerializer:

    @staticmethod
    def serialize(schedule):
        if schedule is None:
            return None

        return {
                   'id': schedule.id,
                   'mon' :  schedule.mon,
                    'tue' : schedule.tue,
                    'wend': schedule.wend,
                    'thur': schedule.thur,
                    'frid': schedule.frid,
                    'satu': schedule.satu,
                    'sun': schedule.sun
               }