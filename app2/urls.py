from app2.views import *
from django.urls import path
app_name='app2'

urlpatterns=[
    path('function2/',function2,name='function2')
]