from django.db import models

# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Division(models.Model):
    name=models.CharField(max_length=100)
    country=models.ForeignKey(Country,on_delete=models.CASCADE, related_name='divisions')
    def __str__(self):
        return self.name
class District(models.Model):
    name=models.CharField(max_length=100)
    division=models.ForeignKey(Division,on_delete=models.CASCADE, related_name='districts')
    def __str__(self):
        return self.name
class SubDistrict(models.Model):
    name=models.CharField(max_length=100)
    district=models.ForeignKey(District,on_delete=models.CASCADE, related_name='subdistricts')
    def __str__(self):
        return self.name