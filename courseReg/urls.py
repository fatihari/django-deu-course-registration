from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('course_registration', views.course_registration, name='course_registration'),
    path('schedule', views.schedule, name='schedule'),
    path('collision_check', views.collision_check, name='collision_check'),
]