from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from swengs.hw1_gruber.models import Plant, Garden
from swengs.hw1_gruber.serializers import PlantSerializer, GardenSerializer


@api_view(['GET','POST'])
def plant_list(request):
    if request.method == 'GET':
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def plant_detail(request, pk):
    try:
        plant = Plant.objects.get(pk=pk)
    except Plant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlantSerializer(plant)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlantSerializer(plant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def garden_list(request):
    if request.method == 'GET':
        garden = Garden.objects.all()
        serializer = GardenSerializer(garden, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GardenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def garden_detail(request, pk):
    try:
        garden = Garden.objects.get(pk=pk)
    except Garden.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GardenSerializer(garden)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GardenSerializer(garden, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        garden.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
