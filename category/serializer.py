
from language.serializer import LanguageSerializer


class CatetorySerializer:

    @staticmethod
    def serialize(category):
        if category is None:
            return None

        return {
                   'id': category.id,
                   'active': category.active,
                   'translated': MultipleCategoriesTranslatorSerializer.serialize(category.categorytranslation_set.all())
               }

class CatetoryTranslationSerializer:

    @staticmethod
    def serialize(category_translator):
        if category_translator is None:
            return None

        return {
                   'name': category_translator.name,
                   'language': LanguageSerializer.serialize(category_translator.language),
               }

class MultipleCategoriesTranslatorSerializer:

    @staticmethod
    def serialize(categories):
        return [CatetoryTranslationSerializer.serialize(category) for category in categories]