from models import Car, CarInstance, UserDetails
from django.contrib.auth.models import User
from datetime import date
import uuid

# AUTOMATIC = 'AU'
# MANUAL = 'MA'
# TRANSMISSION_CHOICES = (
#     (AUTOMATIC, 'Automatic'),
#     (MANUAL, 'Manual'),
# )

# HATCHBACK = 'ha'
# LUXURY_SEDAN = 'lu'
# MPV = 'mv'
# SEDAN = 'se'
# SPORT = 'sp'
# SUV = 'su'
#CUV = 'cu'
# TYPE_CHOICES = (
#     (HATCHBACK, 'Hatchback'),
#     (LUXURY_SEDAN, 'Luxury sedan'),
#     (MPV, 'MPV'),
#     (SEDAN, 'Sedan'),
#     (SPORT, 'Sport'),
#     (SUV, 'SUV'),
#     (CUV, 'Crossover'),
# )

def popz():
	#TOYOTA CARS
	Car.objects.create(make_model="Toyota Corolla Altis", max_passengers=5, transmission="AU", aircon=True, type="se")
	Car.objects.create(make_model="Toyota Corolla Axio", max_passengers=5, transmission="AU", aircon=True, type="se")
	Car.objects.create(make_model="Toyota Camry", max_passengers=5, transmission="AU", aircon=True, type="se")
	Car.objects.create(make_model="Toyota Corona", max_passengers=5, transmission="AU", aircon=True, type="se")
	Car.objects.create(make_model="Toyota AE86", max_passengers=5, transmission="AU", aircon=True, type="sp")
	Car.objects.create(make_model="Toyota Wish", max_passengers=7, transmission="AU", aircon=True, type="mv")
	Car.objects.create(make_model="Toyota Picnic", max_passengers=7, transmission="AU", aircon=True, type="mv")
	Car.objects.create(make_model="Toyota Alphard", max_passengers=6, transmission="AU", aircon=True, type="mv")
	Car.objects.create(make_model="Toyota Vios", max_passengers=5, transmission="AU", aircon=True, type="se")
	Car.objects.create(make_model="Toyota Aurius", max_passengers=5, transmission="AU", aircon=True, type="ha")


	#NISSAN CARS
	Car.objects.create(make_model="Nissan Note", max_passengers=5, transmission="AU", aircon=True, type="mv")
	Car.objects.create(make_model="Nissan Almera", max_passengers=4, transmission="AU", aircon=True, type="se")
	Car.objects.create(make_model="Nissan Sylphy", max_passengers=5, transmission="AU", aircon=True, type="se")
	Car.objects.create(make_model="Nissan Teana", max_passengers=5, transmission="AU", aircon=True, type="lu")
	Car.objects.create(make_model="Nissan Qashqai", max_passengers=5, transmission="MA", aircon=True, type="cu")
	Car.objects.create(make_model="Nissan GT-R", max_passengers=2, transmission="MA", aircon=True, type="sp")
	Car.objects.create(make_model="Nissan 370Z", max_passengers=2, transmission="AU", aircon=True, type="sp")
	Car.objects.create(make_model="Nissan Elgrand", max_passengers=7, transmission="AU", aircon=True, type="mv")
	Car.objects.create(make_model="Nissan Murano", max_passengers=5, transmission="MA", aircon=True, type="su")
	Car.objects.create(make_model="Nissan X-Trail", max_passengers=7, transmission="AU", aircon=True, type="su")

	#HONDA CARS
	Car.objects.create(make_model="Honda Jazz", max_passengers=5, transmission="AU", aircon=True, type="ha")
	Car.objects.create(make_model="Honda Insight", max_passengers=5, transmission="AU", aircon=True, type="ha")
	Car.objects.create(make_model="Honda Accord", max_passengers=5, transmission="AU", aircon=True, type="se")
	Car.objects.create(make_model="Honda City", max_passengers=5, transmission="AU", aircon=True, type="se")
	Car.objects.create(make_model="Honda Civic", max_passengers=5, transmission="AU", aircon=True, type="se")
	Car.objects.create(make_model="Honda Odyssey", max_passengers=7, transmission="AU", aircon=True, type="mv")
	Car.objects.create(make_model="Honda CR-V", max_passengers=5, transmission="AU", aircon=True, type="cu")

	#KIA CARS
	Car.objects.create(make_model="Kia Forte", max_passengers=5, transmission="AU", aircon=True, type="se")
	Car.objects.create(make_model="Kia Cerato", max_passengers=5, transmission="AU", aircon=True, type="se")
	Car.objects.create(make_model="Kia Optima", max_passengers=5, transmission="AU", aircon=True, type="se")
	Car.objects.create(make_model="Kia Sorento", max_passengers=7, transmission="AU", aircon=True, type="su")
	Car.objects.create(make_model="Kia Sportage", max_passengers=5, transmission="AU", aircon=True, type="cu")

	#PORSCHE CARS
	Car.objects.create(make_model="Porsche Boxter", max_passengers=2, transmission="AU", aircon=True, type="sp")
	Car.objects.create(make_model="Porsche Cayman", max_passengers=2, transmission="AU", aircon=True, type="sp")
	Car.objects.create(make_model="Porsche 911 Carrera", max_passengers=2, transmission="MA", aircon=True, type="sp")
	Car.objects.create(make_model="Porsche 918 Spyder", max_passengers=2, transmission="AU", aircon=True, type="sp")
	Car.objects.create(make_model="Porsche Panamera", max_passengers=4, transmission="AU", aircon=True, type="lu")
	Car.objects.create(make_model="Porsche Macan", max_passengers=5, transmission="AU", aircon=True, type="cu")
	Car.objects.create(make_model="Porsche Cayenne", max_passengers=5, transmission="AU", aircon=True, type="cu")

	#MERCEDES CARS
	Car.objects.create(make_model="Mercedes A-Class", max_passengers=5, transmission="AU", aircon=True, type="ha")
	Car.objects.create(make_model="Mercedes B-Class", max_passengers=5, transmission="AU", aircon=True, type="mv")
	Car.objects.create(make_model="Mercedes C-Class", max_passengers=5, transmission="AU", aircon=True, type="se")
	Car.objects.create(make_model="Mercedes CL-Class", max_passengers=5, transmission="AU", aircon=True, type="lu")
	Car.objects.create(make_model="Mercedes E-Class", max_passengers=5, transmission="AU", aircon=True, type="se")
	Car.objects.create(make_model="Mercedes G-Class", max_passengers=5, transmission="AU", aircon=True, type="su")
	Car.objects.create(make_model="Mercedes M-Class", max_passengers=5, transmission="AU", aircon=True, type="su")
	Car.objects.create(make_model="Mercedes R-Class", max_passengers=5, transmission="AU", aircon=True, type="mv")
	Car.objects.create(make_model="Mercedes S-Class", max_passengers=5, transmission="AU", aircon=True, type="lu")
	
	users = ['John', 'Bill', 'Sarah', 'Katie', 'Jim', 'Pierre', 'Claudia', 'Josh', 'Diablo', 'Horace',
			'Ben', 'Quentin', 'William', 'Elrond', 'Richard', 'Tina', 'Jonathan',
			'Carter', 'George', 'Elaine', 'Margery', 'Sam', 'Francis', 'Sylvia',
			'Rhaegar', 'Tammy', 'Oprah', 'Poincare', 'Abel', 'Descarte', 'Fitzgerald',
			'Goldburg', 'Henri', 'Justin', 'Kathryn', "L'hopital", 'Xavier', 'Cauchy']
	
	cars = Car.objects.all()
	cars_length = len(cars)
	cars_start = 0;
	
	colours = ['black', 'silver', 'purple', 'pink', 'yellow', 'blue', 'red', 'orange',
			'green', 'white']
	
	colours_length = len(colours)
	colours_start = 0;
	
	for index, user in enumerate(users):
		email = '%s@%s.com' % (user.lower(), user.lower())
		password = user.lower() + 'password'
		nric = 'S%07d%s' % (index, chr(index%26 + 65))
		dob = date(1970 + index, 1, 1)
		contact = 91111111 + index
		license_issue = date(1990 + index, 1, 1)
		address = user + ' road'
		
		new_user = User.objects.create_user(user, email, password)
		UserDetails.objects.create(user=new_user, nric=nric, dob=dob, 
								contact=contact, license_issue_date=license_issue,
								address=address)
		
		for i in range(0,2):
			CarInstance.objects.create(car=cars[cars_start % cars_length],
									colour=colours[colours_start % colours_length],
									owner=new_user,
									price=(1000 + 50*(cars_start%cars_length)),
									candrivemy=((cars_start%2) == 0),
									year=(1970 + cars_start%10),
									carplate='S%s%s%04d%s' % (chr(cars_start%26 + 65),
														chr((cars_start+5)%26 + 65),
														cars_start,
														chr(((cars_start+cars_start/26)%26 + 65)))
									)
			cars_start += 1
			colours_start += 1
		