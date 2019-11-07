from django.contrib import admin

# Register your models here.
from swengs.hw1_gruber.models import Garden, Plant


class GardenAdmin(admin.ModelAdmin):
    list_display = ('name', 'size','location')

admin.site.register(Garden,GardenAdmin)

class PlantAdmin(admin.ModelAdmin):
    list_display = ('name','color','garden', 'seeded_at','regional','type','quantity')

admin.site.register(Plant,PlantAdmin)

