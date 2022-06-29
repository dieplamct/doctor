from api.exceptions import EntityDoesNotExistException
from .models import District

class DistrictRepo:

    def get_distict(self, id=None):
        try:
            if id is not None:
                return District.objects.get(id=id)    
        except District.DoesNotExist:
            raise EntityDoesNotExistException

    def get_all_district(self):
        try:
            return District.objects.all()
        
        except District.DoesNotExist:
            raise EntityDoesNotExistException
