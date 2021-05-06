from django.urls import path

from portfolio import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('our_works', views.our_works_page, name='our_works'),
    path('about_us', views.about_us, name='about_us'),
]
