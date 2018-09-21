from django.urls import path
from django.conf.urls import include, url
from . import views


urlpatterns = [
    path('', views.competition_list, name='competition_list'),
    path('regulatory/<int:pk>/', views.reg_detail, name='reg_detail'),
    path('add/<int:pk>/', views.add, name='add'),
    path('list/<int:pk>', views.competitor_list, name='lists'),


]
