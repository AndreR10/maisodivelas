from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='news', blank=True)
    category = models.ManyToManyField(Category)
    date_published = models.DateField(default=date.today)

    def __str__(self):
        return self.title