from django.shortcuts import render
from .models import *
import json
# Create your views here.
def indexview(request):
    country=Country.objects.all().order_by('name')
    country_list=list(country.values('name','id'))
    country_list=json.dumps(country_list)

    division=Division.objects.all().order_by('name')
    division_list=list(division.values('name','country__name','id'))
    division_list=json.dumps(division_list)

    district=District.objects.all().order_by('name')
    district_list=list(district.values('name','division__name','id'))
    district_list=json.dumps(district_list)

    subdistrict=SubDistrict.objects.all().order_by('name')
    subdistrict_list=list(subdistrict.values('name','district__name','id'))
    subdistrict_list=json.dumps(subdistrict_list)

    context={
        "country_list":country_list,
        "division_list":division_list,
        "district_list":district_list,
        "subdistrict_list":subdistrict_list,
    }
    return render(request, 'index.html',context)



from .models import Contact
from .serializers import ContactSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
class ContactListCreateAPIView(ListCreateAPIView):
    serializer_class=ContactSerializer
    queryset=Contact.objects.all()
class ContactRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=ContactSerializer
    queryset=Contact.objects.all()
    lookup_field='id'
