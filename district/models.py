from django.db import models

from language.models import Language

class District(models.Model):
    name = models.CharField(max_length=100, blank=True, null=False)
    class Meta:
        db_table = 'district'
        verbose_name = 'District'
        verbose_name_plural = 'District'

    def __str__(self):
        return str(self.name)


class DistrictTranslation(models.Model):
    district=models.ForeignKey('District', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=False)
    language = models.ForeignKey(Language, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'district_translation'
        verbose_name = 'District Translation'
        verbose_name_plural = 'District Translation'

    def __str__(self):
        return str(self.name)