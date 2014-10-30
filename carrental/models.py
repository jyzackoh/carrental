from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

class Car(models.Model):
    """An abstract car type"""
    
    AUTOMATIC = 'AU'
    MANUAL = 'MA'
    TRANSMISSION_CHOICES = (
        (AUTOMATIC, 'Automatic'),
        (MANUAL, 'Manual'),
    )
    
    HATCHBACK = 'ha'
    LUXURY_SEDAN = 'lu'
    MPV = 'mv'
    SEDAN = 'se'
    SPORT = 'sp'
    SUV = 'su'
    TYPE_CHOICES = (
        (HATCHBACK, 'Hatchback'),
        (LUXURY_SEDAN, 'Luxury sedan'),
        (MPV, 'MPV'),
        (SEDAN, 'Sedan'),
        (SPORT, 'Sport'),
        (SUV, 'SUV'),
    )
    
    make_model = models.CharField(max_length=128, primary_key=True)
    max_passengers = models.IntegerField()
    transmission = models.CharField(choices=TRANSMISSION_CHOICES,
                                    max_length=2,
                                    default=AUTOMATIC)
    aircon = models.BooleanField()
    type = models.CharField(choices=TYPE_CHOICES,
                            max_length=2)
    
class CarInstance(models.Model):
    car = ForeignKey('Car', on_delete=models.CASCADE)
    colour = models.CharField(max_length=128)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    candrivemy = models.BooleanField()
    year = models.IntegerField()    
    carplate = models.CharField(max_length=16, primary_key=True)
    
class Booking(models.Model):
    start = models.DateField()
    end = models.DateField()
    car_instance = ForeignKey('CarInstance', on_delete=models.CASCADE)
    borrower = ForeignKey(User, on_delete=models.CASCADE)
    
class UserDetails(models.Model):
    user = models.OneToOneField(User)
    nric = models.CharField(max_length=9)
    dob = models.DateField()
    contact = models.CharField(max_length=8)
    license_issue_date = models.DateField()
    address = models.CharField(max_length=512)