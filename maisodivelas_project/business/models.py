from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=30)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=256)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    email = models.EmailField(max_length=256)
    description = models.TextField()
    image = models.ImageField(default="images/business_default.png",
                              upload_to='business')
    sub_sector = models.ManyToManyField(SubCategory)
    date_created = models.DateField(default=date.today)

    def __str__(self):
        return self.name
