from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home_view, name='home'),
    path('<int:id>/detail/', views.detail_view, name='detail'),
]
