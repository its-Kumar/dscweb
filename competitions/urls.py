from django.urls import path
from . import views

app_name = 'competitions'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('<int:pk>-<str:slug>/', views.detail_view, name='detail'),
]
