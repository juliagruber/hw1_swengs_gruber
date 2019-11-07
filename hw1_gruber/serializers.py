from rest_framework import serializers

from swengs.hw1_gruber.models import Plant, Garden


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['name','color','garden', 'seeded_at','regional','type','quantity']


class GardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garden
        fields = ['name', 'size','location']