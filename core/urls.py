from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('map/', views.map_view, name='map'),
    path('calculator/', views.calculator, name='calculator'),
    path('info/', views.info, name='info'),
    path('api/facilities/', views.get_facilities_json, name='facilities_json'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
