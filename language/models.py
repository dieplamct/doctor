from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=255, blank=True, null=False)
    short_name = models.CharField(max_length=2, blank=True, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return str(self.name)
