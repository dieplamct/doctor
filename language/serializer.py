
class LanguageSerializer:

    @staticmethod
    def serialize(language):
        if language is None:
            return None

        return {
                   'id': language.id,
                   'name': language.name,
                   'short_name': language.short_name,
               }