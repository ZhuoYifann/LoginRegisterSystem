
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.signout, name='signout'),
]