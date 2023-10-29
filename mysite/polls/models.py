from django.db import models

# Create your models here.
class Language(models.Model):
    language = models.CharField(max_length=255)
    knowledge = models.IntegerField()
    description = models.CharField(max_length=2000)
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return f'{self.language}'