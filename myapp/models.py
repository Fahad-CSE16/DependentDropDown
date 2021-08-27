from django.db import models

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

class Address(models.Model):
    addressOf=models.CharField(max_length=100)
    country=models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='country_set')
    division=models.ForeignKey(Division, on_delete=models.SET_NULL, null=True, blank=True, related_name='division_set')
    district=models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True, related_name='district_set')
    subdistrict=models.ForeignKey(SubDistrict, on_delete=models.SET_NULL, null=True, blank=True, related_name='subdistrict_set')
    def __str__(self):
        return self.addressOf




class Contact(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=17)
    email=models.EmailField()
    text=models.TextField()
    def __str__(self):
        return self.name