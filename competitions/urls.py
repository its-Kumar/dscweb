from django.urls import path
from . import views

app_name = 'competitions'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('dscblend',views.dscblend,name='dscblend'),
    
   

]
