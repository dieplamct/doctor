from django.db import models

from doctor.models import Doctor
from language.models import Language

class Schedule(models.Model):
    mon = models.CharField(max_length=100, blank=True, null=True)
    tue = models.CharField(max_length=100, blank=True, null=True)
    wend = models.CharField(max_length=100, blank=True, null=True)
    thur = models.CharField(max_length=100, blank=True, null=True)
    frid = models.CharField(max_length=100, blank=True, null=True)
    satu = models.CharField(max_length=100, blank=True, null=True)
    sun = models.CharField(max_length=100, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'schdule'
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedule'

    def __str__(self):
        return str(self.doctor)
