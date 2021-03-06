from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
import uuid

AUTOMATIC = 'AU'
MANUAL = 'MA'
NONE = 'na'

TRANSMISSION_CHOICES = (
	(NONE, 'Select transmission'),
	(AUTOMATIC, 'Automatic'),
	(MANUAL, 'Manual'),
)

HATCHBACK = 'ha'
LUXURY_SEDAN = 'lu'
MPV = 'mv'
SEDAN = 'se'
SPORT = 'sp'
SUV = 'su'
CUV = 'cu'


TYPE_CHOICES = (
	(NONE, 'Select type'),
	(HATCHBACK, 'Hatchback'),
	(LUXURY_SEDAN, 'Luxury sedan'),
	(MPV, 'MPV'),
	(SEDAN, 'Sedan'),
	(SPORT, 'Sport'),
	(SUV, 'SUV'),
	(CUV, 'Crossover'),
)

class Car(models.Model):
	"""An abstract car type"""
	
	make_model = models.CharField(max_length=128, primary_key=True)
	max_passengers = models.IntegerField()
	transmission = models.CharField(choices=TRANSMISSION_CHOICES,
									max_length=2,
									default=AUTOMATIC)
	aircon = models.BooleanField()
	type = models.CharField(choices=TYPE_CHOICES,
							max_length=2)
	
	def __unicode__(self):
		return self.make_model
	
class CarInstance(models.Model):
	car = ForeignKey('Car', on_delete=models.CASCADE)
	colour = models.CharField(max_length=128)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	price = models.DecimalField(decimal_places=2, max_digits=10)
	candrivemy = models.BooleanField()
	year = models.IntegerField()
	carplate = models.CharField(max_length=16, primary_key=True)
	
	def __unicode__(self):
		return self.carplate
	
class Booking(models.Model):
	uuid = models.CharField(max_length=36, unique=True, default=uuid.uuid4, editable=False)
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
	
	class Meta:
		verbose_name_plural = 'User Details'