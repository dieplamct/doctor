from django.db import models

from language.models import Language

class District(models.Model):
    name = models.CharField(max_length=255, blank=True, null=False)
    language_id = models.ForeignKey(Language, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'District'
        verbose_name_plural = 'District'

    def __str__(self):
        return str(self.name)
