from forms import CustomRegistrationForm, UserDetailsForm, AddCarInstanceForm, SelectCarForm, ChangeEmailForm, ChangeBookingForm, ChangeUserDetailsForm, SearchCarForm, MoreDetailedSearchCarForm, RentCarForm
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from models import CarInstance, Booking
from django import forms
from datetime import datetime
from django.db.models import Q

def index(request):
	form = SearchCarForm()
	more_detailed_search_car_form = MoreDetailedSearchCarForm()
	return render(request, 'index.html', {'user_id': request.user, 
										'form': form, 
										'more_detailed_form': more_detailed_search_car_form})

def search(request):
	car_qrs = None
	print "inside search"
	if request.method == 'GET': #create new user
		print 'inside request method'
		form = MoreDetailedSearchCarForm(request.GET)
		if form.is_valid():
			print "inside form is valid"
			flag = False;
			cleaned_data = form.cleaned_data
			car = cleaned_data['car']
			start = cleaned_data['price_lower']
			end = cleaned_data['price_upper']
			colour = cleaned_data['colour']
			candrivemy = cleaned_data['candrivemy']
			year = cleaned_data['year']
			passengers = cleaned_data['passengers']
			type = cleaned_data['type']
			transmission = cleaned_data["transmission"]
			aircon = cleaned_data['aircon']
			
			ordering = cleaned_data['ordering']
			ascending = cleaned_data['ascending']
			
			q = Q()
			if car:
				print "car"
				q &= Q(car__make_model__icontains=car)
				flag = True;
			if start:
				print "start"
				q &= Q(price__gte=start)
				flag = True;
			if end:
				print "end"
				q &= Q(price__lte=end)
				flag=True
			if colour:
				print "color"
				q &= Q(colour__iexact=colour)
				flag = True;
			if candrivemy is not None:
				print "candrivemy"
				q &= Q(candrivemy=candrivemy)
				flag = True;
			if year:
				print "year"
				q &= Q(year=year)
				flag = True;
			if passengers:
				print "passengers"
				q &= Q(car__max_passengers__gte=passengers)
				flag = True;
			if type and type != 'na':
				print "type " + type
				q &= Q(car__type=type)
				flag = True;
			if transmission and transmission != 'na':
				print "transmission"
				q &= Q(car__transmission=transmission)
				flag = True;
			if aircon is not None:
				print "aircon"
				q &= Q(car__aircon=aircon)
				flag= True
			if (flag):
				car_qrs = CarInstance.objects.filter(q)
				
				if ordering:
					print "ordering!"
					print ordering
					if ascending:
						print 'ascending!'
						print ascending
						car_qrs = car_qrs.order_by(ordering)
					else:
						print "descending!"
						car_qrs = car_qrs.order_by('-' + ordering)
			else:
				car_qrs = None

			form = SearchCarForm()
			more_detailed_search_car_form = MoreDetailedSearchCarForm()
			resubmit_form = MoreDetailedSearchCarForm(request.GET)

	return render(request, 'search.html', {'user_id': request.user, 'cars': car_qrs, 
										'more_detailed_form': more_detailed_search_car_form,
										'form':form,
										'resubmit_form': resubmit_form})

def car_info(request):
	carplate = request.GET.get('id', None)
	cars = CarInstance.objects.all()
	car_qrs = CarInstance.objects.filter(carplate=carplate)
	return render(request, 'car_info.html', {'user_id': request.user, 'car': car_qrs})

@login_required
def account(request): #This one surely must login.
	user_qrs = list(User.objects.filter(username=request.user))
	user_qrs = user_qrs[0]
	show = request.GET.get('show', 'my-account')
	error = request.GET.get('error', None)
	start = request.GET.get('start', None)
	end = request.GET.get('end', None)
	error_msg_owned = None
	error_msg_rented = None

	if error == '1':
		error_msg_owned = "Unable to delete car listing as it is being rented at the moment!"
	elif error == '2':
		error_msg_owned = "Unable to delete car listing as you don't own the car!"
	elif error == '3':
		error_msg_owned = "Unable to delete car listing as it does not exist!"
	elif error == '4':
		error_msg_rented = "Unable to delete booking as it is ongoing!"
	elif error == '5':
		error_msg_rented = "Unable to delete booking as you are not the borrower!"
	elif error == '6':
		error_msg_rented = "Unable to delete booking as it does not exist!"
	elif error == '7':
		error_msg_rented = "Your Request was not understood! Please contact admin for assistance."
	elif error == '8':
		error_msg_rented = "Unable to modify booking as it is ongoing!"
	elif error == '9':
		error_msg_rented = "Unable to modify booking as car is not available from " + start + "to " + end + "!"
	elif error == '10':
		error_msg_rented = "Unable to modify booking as you are not the borrower!"

	if request.method == 'POST': #create new user
		car_form = SelectCarForm(request.POST)
		form = AddCarInstanceForm(request.POST)
		if form.is_valid() and car_form.is_valid():
			car = (dict(car_form.cleaned_data))['car']
			car_instance = form.save(commit=False)
			car_instance.owner = user_qrs
			car_instance.car = car
			car_instance.save()

	form = AddCarInstanceForm()
	car_form = SelectCarForm()
	car_instances = CarInstance.objects.filter(owner=user_qrs)
	bookings = Booking.objects.filter(borrower=user_qrs)
	owned_bookings = Booking.objects.filter(car_instance__owner=user_qrs)

	return render(request, "registration/account.html", {
		'form': form,
		'car_form': car_form,
		'car_instances': car_instances,
		'bookings': bookings,
		'owned_bookings': owned_bookings,
		'user_details': user_qrs, 
		'user_id': request.user,
		'show': show,
		'error_owned': error_msg_owned,
		'error_rented': error_msg_rented,
	})

	# user_qrs = list(User.objects.filter(username=request.user))
	# user_qrs = user_qrs[0]
	# #pass in owned cars
	# #pass in rented cars
	# return render(request, 'registration/account.html', {'user_details': user_qrs, 'user_id': request.user})

def account_public(request, username): #Public's view of person's profile
	#If User wants to see his own profile
	if (str(request.user) == str(username)):
		return redirect('/accounts/user/')

	user_qrs = list(User.objects.filter(username=username))
	
	#No Such User
	if (len(user_qrs) == 0):
		user_qrs = {}
		user_qrs['username'] = username
		return render(request, 'registration/account_public.html', {'valid':False, 'user_details': user_qrs})   
	
	user_qrs = user_qrs[0]
	owned_cars = CarInstance.objects.filter(owner=user_qrs)
	#pass in rented cars

	return render(request, 'registration/account_public.html', {'valid':True, 'user_details': user_qrs, 'user_id': request.user, 'owned_cars': owned_cars})

@login_required
def rent(request): #This is the processor for renting the car itself. For this, user MUST be logged in.
	if request.method == 'GET':
		form = RentCarForm(request.GET)
		if form.is_valid():
			cleaned_data = form.cleaned_data
			carplate = cleaned_data['carplate']
			start = cleaned_data['dateStart']
			end = cleaned_data['dateEnd']

			start = (datetime.strptime(start, "%Y/%m/%d")).date()
			end = (datetime.strptime(end, "%Y/%m/%d")).date()


			#Check if the car exists
			car_instance = list(CarInstance.objects.filter(carplate=carplate))
			if (len(car_instance) > 0):
				car_instance = car_instance[0]
			else:
				car_instance = None

			#Check if user is owner
			if (car_instance):
				user_qrs = list(User.objects.filter(username=request.user))
				user_qrs = user_qrs[0]
				if (user_qrs == car_instance.owner):
					return render(request, 'rent.html', {'valid':False, 'available': False, 'start':start, 'end':end, 'carplate':carplate})

			#check if can rent first
			q = Q()
			q &= Q(car_instance__carplate=carplate)
			q &= Q(start__gte=start)
			q &= Q(end__lte=end)

			clashed_bookings = list(Booking.objects.filter(q))

			#availability check
			if (len(clashed_bookings) == 0):
				Booking.objects.create(start=start, end=end, car_instance=car_instance, borrower=user_qrs)
				return render(request, 'rent.html', {'valid':True, 'available': True, 'start':start, 'end':end, 'carplate':carplate})
			else:
				return render(request, 'rent.html', {'valid':True, 'available': False, 'start':start, 'end':end, 'carplate':carplate})

	return redirect("/")


def register(request):
	if request.method == 'POST': #create new user
		form = CustomRegistrationForm(request.POST)
		user_details_form = UserDetailsForm(request.POST)
		if form.is_valid() and user_details_form.is_valid():
			user = form.save()
			user_details = user_details_form.save(commit=False)
			user_details.user = user
			user_details.save()
			return HttpResponseRedirect("/accounts/user")
	else:
		form = CustomRegistrationForm()
		user_details_form = UserDetailsForm()
	return render(request, "registration/register.html", {
		'form': form,
		'user_details_form':user_details_form,
	})


@login_required
def modify(request): #This one surely must login.
	user_qrs = list(User.objects.filter(username=request.user))
	user_qrs = user_qrs[0]
	flag = False

	change_email_form = ChangeEmailForm(request.GET)
	change_user_details_form = ChangeUserDetailsForm(request.GET)

	if (change_email_form.is_valid()):
		new_email = (dict(change_email_form.cleaned_data))['email']
		if (new_email):
			user_qrs.email = new_email
			user_qrs.save()

	if (change_user_details_form.is_valid()):
		contact = (dict(change_user_details_form.cleaned_data))['contact']
		address = (dict(change_user_details_form.cleaned_data))['address']
		if (contact):
			user_qrs.userdetails.contact = contact
			flag = True

		if (address):
			user_qrs.userdetails.address = address
			flag = True

		if (flag):
			user_qrs.userdetails.save()

	return redirect("/accounts/user")


@login_required
def modify_booking(request): #This one surely must login.
	user_qrs = (list(User.objects.filter(username=request.user)))[0]
	booking = None
	today = datetime.now()

	#Check if form valid
	change_booking_form = ChangeBookingForm(request.GET)
	if (change_booking_form.is_valid()):
	
		#Get the data
		keys = (dict(change_booking_form.cleaned_data))
		new_start = keys['dateStart']
		new_end = keys['dateEnd']
		uuid = keys['uuid_hidden']

		new_start = (datetime.strptime(new_start, "%Y/%m/%d")).date()
		new_end = (datetime.strptime(new_end, "%Y/%m/%d")).date()

		print(new_start)
		print(new_end)
		print(uuid)

		#Only assign booking iff booking is before or after today
		q = Q()
		q &= Q(uuid=uuid)
		q2 = Q(start__gt=today)
		q2 |= Q(end__lt=today)
		q &= q2
		booking = list(Booking.objects.filter(q))
		if (len(booking) > 0):
			booking = booking[0]
		else:
			booking = None;

		#availability check
		if (booking):		
			#check if car available on new date range
			q = Q()
			q &= Q(car_instance__carplate=booking.car_instance.carplate)
			q &= Q(start__gte=new_start)
			q &= Q(end__lte=new_end)
			clashed_bookings = list(Booking.objects.filter(q))


			if (len(clashed_bookings) == 0): #new period is available and the booking is not ongoing
				if (booking.borrower == user_qrs):
					booking.start = new_start
					booking.end = new_end
					booking.save()
					return redirect("/accounts/user?show=my-rented-cars")
				else:
					return redirect("/accounts/user?show=my-rented-cars&error=10") #item does not belong to you
			else:
				return redirect("/accounts/user?show=my-rented-cars&error=9&start="+new_start+"&end="+new_end) #Some error saying the chosen date is unavailable
		else:
			return redirect("/accounts/user?show=my-rented-cars&error=8") #some error message saying the booking is ongoing.

	return redirect("/accounts/user?show=my-rented-cars&error=7") #invalid request

@login_required
def remove_booking(request): #This one surely must login.
	user_qrs = (list(User.objects.filter(username=request.user)))[0]
	uuid = request.GET.get('uuid', None)
	booking = None
	today = datetime.now()
	if (uuid):
		q = Q()
		q &= Q(uuid=uuid)
		q2 = Q(start__gt=today)
		q2 |= Q(end__lt=today)
		q &= q2
		booking = list(Booking.objects.filter(q))
		if (len(booking) > 0):
			booking = booking[0]
	else:
		return redirect("/accounts/user?show=my-rented-cars&error=6")

	if (booking):
		if (booking.borrower == user_qrs):
			booking.delete()
			return redirect("/accounts/user?show=my-rented-cars")
		else:
			return redirect("/accounts/user?show=my-rented-cars&error=5")

	return redirect("/accounts/user?show=my-rented-cars&error=4")

@login_required
def remove_car(request): #This one surely must login.
	user_qrs = (list(User.objects.filter(username=request.user)))[0]
	carplate = request.GET.get('id', None)
	car_instance = None
	today = datetime.now()
	if (carplate):
		q = Q()
		q &= Q(car_instance__carplate=carplate)
		q &= Q(start__lte=today)
		q &= Q(end__gte=today)
		booking = list(Booking.objects.filter(q))
		if (len(booking) > 0):
			#cannot delete
			return redirect("/accounts/user/?show=my-cars&error=1")
		else:
			#No clashes, delete if user is owner!
			car_instance = (list(CarInstance.objects.filter(carplate=carplate)))[0]
			if (car_instance.owner == user_qrs):
				car_instance.delete()
				return redirect("/accounts/user/?show=my-cars")
			else:
				return redirect("/accounts/user/?show=my-cars&error=2")

	return redirect("/accounts/user/?show=my-cars&error=3")
