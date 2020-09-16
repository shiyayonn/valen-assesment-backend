from django.conf.urls import url 
from api.views import car_list, car_list_by_color
from django.urls import path

urlpatterns = [ 
    path('api/cars', car_list),
    path('api/cars/<str:car_color>',car_list_by_color)
]