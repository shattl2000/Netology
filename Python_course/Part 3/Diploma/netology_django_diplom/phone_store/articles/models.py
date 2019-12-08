from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
from pytils.translit import slugify


class Article(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    products = models.ManyToManyField(Product, related_name='articles')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    pub_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        slug = slugify(self.title)
        if len(slug) > 50:
            slug = slug[:50]
        self.slug = slug
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
