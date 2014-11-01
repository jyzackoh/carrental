from models import Car



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
# TYPE_CHOICES = (
#     (HATCHBACK, 'Hatchback'),
#     (LUXURY_SEDAN, 'Luxury sedan'),
#     (MPV, 'MPV'),
#     (SEDAN, 'Sedan'),
#     (SPORT, 'Sport'),
#     (SUV, 'SUV'),
# )

def popz():
	#TOYOTA CARS
	Car.objects.create(make_model="Toyota Corolla Altis", max_passengers=5, transmission="AU", aircon=True, type="se")
	Car.objects.create(make_model="Toyota Corolla Axio", max_passengers=5, transmission="AU", aircon=True, type="se")
	Car.objects.create(make_model="Toyota Camry", max_passengers=5, transmission="AU", aircon=True, type="se")
	Car.objects.create(make_model="Toyota Corona", max_passengers=5, transmission="AU", aircon=True, type="se")
	Car.objects.create(make_model="Toyota AE86", max_passengers=5, transmission="AU", aircon=True, type="sp")
	Car.objects.create(make_model="Toyota Wish", max_passengers=7, transmission="AU", aircon=True, type="mpv")
	Car.objects.create(make_model="Toyota Picnic", max_passengers=7, transmission="AU", aircon=True, type="mpv")
	Car.objects.create(make_model="Toyota Alphard", max_passengers=6, transmission="AU", aircon=True, type="mpv")
	Car.objects.create(make_model="Toyota Vios", max_passengers=5, transmission="AU", aircon=True, type="se")
	Car.objects.create(make_model="Toyota Aurius", max_passengers=5, transmission="AU", aircon=True, type="ha")


	# #NISSAN CARS
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")

	# #HONDA CARS
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")

	# #KIA CARS
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")

	# #PORSCHE CARS
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")

	# #MERCEDES CARS
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")
	# Car.objects.create(make_model="Toyota Corolla", max_passengers=5, transmission="AU", aircon=True, type="se")