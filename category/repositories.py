from unicodedata import category
from api.exceptions import EntityDoesNotExistException
from .models import Category, CategoryTranslation

class CategoryRepo:

    def _decode_db_category(self, db_category):
        return Category(id=db_category.id,
                          active=db_category.active)

    def get_category(self, category_id=None):
        try:
            category = Category.objects.get(id=category_id)
            return self._decode_db_category(category)
        except Category.DoesNotExist:
            raise EntityDoesNotExistException

    def get_all_category(self):
        try:
            return Category.objects.all()
        
        except Category.DoesNotExist:
            raise EntityDoesNotExistException


class CategoryTranslatorRepo:

    def _decode_db_category_translator(self, db_category_translator):
        return CategoryTranslation(id=db_category_translator.id,
                          name=db_category_translator.name,
                          category=db_category_translator.category,
                          language=db_category_translator.language)

    def get_category_translator(self, catetory_id=None):
        try:
            category_translator = CategoryTranslation.objects.select_related('category').get(id=catetory_id)    
            return self._decode_db_category_translator(category_translator)
        except CategoryTranslation.DoesNotExist:
            raise EntityDoesNotExistException

    def get_all_category_by_language(self, language_id):
        try:
            return CategoryTranslation.objects.get(language_id=language_id)
        
        except CategoryTranslation.DoesNotExist:
            raise EntityDoesNotExistException