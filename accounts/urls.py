from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signupPage, name='signup'),
    path('account/', views.account_settings, name='account'),
]
