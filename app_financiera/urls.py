from django.urls import path
from . import views

app_name = 'financiera'

urlpatterns = [
    path('', views.index, name='index'),

]