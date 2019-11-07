from django.urls import path
from swengs.hw1_gruber import views

urlpatterns = [
    path('plants/', views.plant_list),
    path('plant/<int:pk>/', views.plant_detail),
    path('gardens/', views.garden_list),
    path('garden/<int:pk>/', views.garden_detail),
]
