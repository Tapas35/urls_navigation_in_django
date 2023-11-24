from app1.views import *
from django.urls import path
app_name='app1'

urlpatterns=[
    path('function1/',function1,name='function1')
   
]