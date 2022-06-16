from django.db import models

class District(models.Model):
    name = models.CharField(max_length=255, blank=True, null=False)

    class Meta:
        verbose_name = 'District'
        verbose_name_plural = 'District'

    def __str__(self):
        return str(self.name)
