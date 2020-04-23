from django.urls import path
from . import views

app_name = 'workshops'
urlpatterns = [
    path('', views.home_view, name='home'),

]