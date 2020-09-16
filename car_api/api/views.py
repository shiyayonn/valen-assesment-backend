from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from api.models import Car
from api.serializers import CarSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'PUT'])
def car_list(request):

    if request.method == 'GET':
        cars = Car.objects.all()
        car_serializer = CarSerializer(cars, many = True)
            
        return JsonResponse(car_serializer.data, safe = False)

    elif request.method == 'POST':
        car_data = JSONParser().parse(request)
        car_serializer = CarSerializer(data = car_data)
        
        if car_serializer.is_valid():
            
            if Car.objects.filter(name=car_data['name']).count()!=0:
                return JsonResponse({"Error":"Car already exist"})
                
            car_serializer.save()
            return JsonResponse(car_serializer.data, status = status.HTTP_201_CREATED)
        
        return JsonResponse(car_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    elif request.method == 'PUT':
        details = JSONParser().parse(request)
        car_1 = Car.objects.get(name=details['name_1'])
        car_2 = Car.objects.get(name=details['name_2'])
        temp = car_1.name
        car_1.name = car_2.name
        car_2.name = temp
        car_1.save()
        car_2.save()
        return JsonResponse({"Success":"Cars have been swapped"})

@api_view(['GET'])
def car_list_by_color(request,car_color):
    
    if request.method == "GET":
        cars = Car.objects.filter(color=car_color)
        car_serializer = CarSerializer(cars, many = True)
        return JsonResponse(car_serializer.data,safe=False)