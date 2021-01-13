from django.db import models
from phone_field import PhoneField
# Create your models here.

class All_Direction(models.Model):
    name = models.CharField(('name'),max_length=120)

    def __str__(self):
        return self.name


class Direction(models.Model):
    name=models.CharField(('name'),max_length=120)
    all_diriction_id=models.ForeignKey(All_Direction,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Users(models.Model):
    username=models.CharField(('username'),max_length=80)
    FIO=models.CharField(('FIO'),max_length=120)
    data=models.DateField(("data"),'2000-10-14')
    address=models.CharField(('address'),max_length=120)
    place_of_study=models.CharField(('place_of_study'),max_length=200)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    all_Direction_id=models.ManyToManyField(All_Direction)

    def __str__(self):
        return self.username