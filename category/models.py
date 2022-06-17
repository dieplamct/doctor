from django.db import models

from language.models import Language

class Category(models.Model):
    active = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cateory'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.name)


class CategoryTranslation(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category_translation'
        verbose_name = 'Category Translation'
        verbose_name_plural = 'Categorie Translation'

    def __str__(self):
        return str(self.name)
