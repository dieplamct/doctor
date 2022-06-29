from api.exceptions import EntityDoesNotExistException
from .models import Language

class LanguageRepo:

    def _decode_db_language(self, db_language):
        return Language(id=db_language.id,
                          name=db_language.name,
                          short_name=db_language.short_name)

    def get_language(self, language_id=None):
        try:
            language = Language.objects.get(id=language_id)
            return self._decode_db_language(language)
        except Language.DoesNotExist:
            raise EntityDoesNotExistException

    def get_all_language(self):
        try:
            return Language.objects.all()
        
        except Language.DoesNotExist:
            raise EntityDoesNotExistException
