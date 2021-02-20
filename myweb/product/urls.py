from django.urls import path
from .views import about,cstmrdata_save

urlpatterns=[
    path('get',about),
    path('save',cstmrdata_save)
] 