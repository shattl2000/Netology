from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    image = models.URLField()
    release_date = models.DateField()
    price = models.CharField(max_length=100)
    lte_exists = models.BooleanField()
    slug = models.SlugField(verbose_name='slug', unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)