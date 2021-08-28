from django.db import models
from myapp.models import Country, Division, District, SubDistrict
from django.contrib.auth.models import User
class Location(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='location')
    phone=models.CharField(max_length=100,blank=True, null= True)
    country=models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True, related_name='cntry')
    division=models.ForeignKey(Division, on_delete=models.SET_NULL, blank=True, null=True, related_name='dvsn')
    district=models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True, related_name='dstrct')
    subdistrict=models.ForeignKey(SubDistrict, on_delete=models.SET_NULL, blank=True, null=True, related_name='sbdstrct')
    