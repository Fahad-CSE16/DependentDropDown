from django.urls import path
from .views import *
urlpatterns = [
    path('divisions/',DivisionList.as_view()),
    path('districts/',DistrictList.as_view()),
    path('subdistricts/',SubDistrictList.as_view()),
]
