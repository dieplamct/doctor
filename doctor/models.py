from django.db import models
from category.models import Category

from district.models import District
from language.models import Language

class Doctor(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    district = models.ForeignKey(District, null=True)
    fee = models.DecimalField(max_digits=19, decimal_places=2)
    schedule = models.JSONField(blank=True)
    category = models.ForeignKey(Category, db_index=True)
    language = models.ForeignKey(Language, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctor'

    def __str__(self):
        return str(self.name)
