from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('our_works', views.our_works_page, name='our_works')
]
