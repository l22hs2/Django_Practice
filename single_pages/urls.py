from django.urls import path

from single_pages import views

urlpatterns = [
    path('', views.landing),
    path('about_me/', views.about_me),
]