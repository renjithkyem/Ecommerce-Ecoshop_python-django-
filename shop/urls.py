
from django.urls import path
from . import views
from shop import views

urlpatterns = [
    path('',views.shop, name='shop'),
]
