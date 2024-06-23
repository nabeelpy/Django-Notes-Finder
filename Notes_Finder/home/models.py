from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=64)
    currency = models.CharField(max_length=64)
    currency_sign = models.CharField(max_length=64)

    def __str__(self):
       return self.name

class Color(models.Model):
        color_name = models.CharField(max_length=64)
        color_hex = models.CharField(max_length=64)
        color_hex2 = models.CharField(max_length=64, default='')

        def __str__(self):
            return self.color_name

class Note(models.Model):
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    color_id = models.ForeignKey(Color, on_delete=models.CASCADE)
    note = models.CharField(max_length=100)
    remarks = models.CharField(max_length=1000)
    length = models.IntegerField()
    width = models.IntegerField()
    front_img = models.ImageField(upload_to = 'static/')
    back_img = models.ImageField(upload_to = 'static/')


    def __str__(self):
        return self.note
