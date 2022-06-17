from django.db import models
from category.models import Category

from district.models import District

class Doctor(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    district = models.ForeignKey(District, null=True, on_delete=models.CASCADE)
    fee = models.DecimalField(max_digits=19, decimal_places=2)
    category = models.ForeignKey(Category, db_index=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'doctor'
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctor'

    def __str__(self):
        return str(self.name)
