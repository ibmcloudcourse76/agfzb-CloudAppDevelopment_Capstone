from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='Make')
    description = models.CharField(max_length=200, default='Description')
    
    def __str__(self):
        return "Name: " + self.name + ", " + \
               "Description: " + self.description

class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    id = models.IntegerField(default=1,primary_key=True)
    name = models.CharField(null=False, max_length=30, default='Car')

    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon')
    ]
    type = models.CharField(
        null=False,
        max_length=50,
        choices=CAR_TYPES,
        default=SEDAN
    )

    year = models.DateField(default=now)

    def __str__(self):
        return "Dealer ID: " + self.id + ", " + \
               "Name: " + self.name + ", " + \
               "Type: " + self.type + ", " + \
               "Year: " + str(self.year)


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
