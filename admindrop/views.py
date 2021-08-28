from django.http.response import JsonResponse
from myapp.models import Country, District, Division
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
class DivisionList(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        country=request.data['country']
        division={}
        if country:
            divisions=Country.objects.get(id=country).divisions.all()
            division={p.name:p.id for p in divisions}
        return JsonResponse(data=division, safe=False)
class DistrictList(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        division=request.data['division']
        district={}
        if division:
            districts=Division.objects.get(id=division).districts.all()
            district={p.name:p.id for p in districts}
        return JsonResponse(data=district, safe=False)
class SubDistrictList(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        district=request.data['district']
        subdistrict={}
        if district:
            subdistricts=District.objects.get(id=district).subdistricts.all()
            subdistrict={p.name:p.id for p in subdistricts}
        return JsonResponse(data=subdistrict, safe=False)
