from django.db import models
from django.conf import settings
from phone_field import PhoneField
from localflavor.pl.forms import PLPostalCodeField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


INSTITUTION_TYPES = {
    (1, "Fundacja"),
    (2, "Organizacja pozarządowa"),
    (3, "Zbiórka lokalna"),
}


class Institution(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    type = models.IntegerField(choices=INSTITUTION_TYPES, default=1)
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField('Category')
    institution = models.ForeignKey('Institution', null=True, on_delete=models.SET_NULL)
    address = models.TextField()
    phone_number = PhoneField(help_text='Contact phone number')
    city = models.TextField()
    zip_code = PLPostalCodeField()
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    pickup_comment = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.city} - {self.pickup_date} - QTY:{self.quantity}"








