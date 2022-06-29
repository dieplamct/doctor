
from language.serializer import LanguageSerializer


class DistrictSerializer:

    @staticmethod
    def serialize(distict):
        if distict is None:
            return None

        return {
                   'id': distict.id,
                   'name': distict.name,
                   'translated': MultipleDistrictsTranslatorSerializer.serialize(distict.districttranslation_set.all())
               }

class DistrictTranslationSerializer:

    @staticmethod
    def serialize(distict_translator):
        if distict_translator is None:
            return None

        return {
                   'name': distict_translator.name,
                   'language': LanguageSerializer.serialize(distict_translator.language),
               }

class MultipleDistrictsTranslatorSerializer:

    @staticmethod
    def serialize(disticts):
        return [DistrictTranslationSerializer.serialize(distict) for distict in disticts]