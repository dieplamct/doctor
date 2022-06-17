from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=255, blank=True, null=False)
    short_name = models.CharField(max_length=2, blank=True, null=False)

    class Meta:
        db_table = 'language'
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return "{} - {} - {}" .format(str(self.id), str(self.name), str(self.short_name))

    def get_instance(self):
        return self
