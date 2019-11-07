from django.db import models

# Create your models here.


class Garden(models.Model):
    name = models.TextField()
    size = models.PositiveIntegerField(help_text="in square meter")
    location = models.TextField()

    def __str__(self):
        return self.name



class Plant(models.Model):

    CHOICES = (
        ('ve' , 'Vegetable'),
        ('fr' , 'Fruit'),
        ('fl' , 'Flower'),
    )

    name = models.TextField()
    color = models.TextField()
    garden = models.ForeignKey(Garden,on_delete=models.CASCADE)
    seeded_at = models.DateField()
    regional = models.BooleanField()
    type = models.CharField(max_length=2,choices=CHOICES)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


