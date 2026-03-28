from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('pin/', views.pinpage, name='pinpage'),
    path('final/', views.finalpage, name='finalpage'),
]