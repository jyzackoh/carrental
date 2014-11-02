from forms import CustomRegistrationForm, UserDetailsForm, AddCarInstanceForm, SelectCarForm, changeEmailForm, changeUserDetailsForm, SearchCarForm, MoreDetailedSearchCarForm
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from models import CarInstance
from django import forms
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
			
			q = Q()
			if car:
				print "car"
				q &= Q(car__make_model__icontains=car)
			if start:
				print "start"
				q &= Q(price__gte=start)
			if end:
				print "end"
				q &= Q(price__lte=end)
			if colour:
				print "color"
				q &= Q(colour__iexact=colour)
			if candrivemy:
				print "candrivemy"
				q &= Q(candrivemy=candrivemy)
			if year:
				print "year"
				q &= Q(year=year)
			if passengers:
				print "passengers"
				q &= Q(car__max_passengers__gte=passengers)
			if type and type != 'na':
				print "type " + type
				q &= Q(car__type=type)
			if transmission and transmission != 'na':
				print "transmission"
				q &= Q(car__transmission=transmission)
				
			car_qrs = CarInstance.objects.filter(q)

	return render(request, 'search.html', {'user_id': request.user, 'cars': car_qrs})


def car_info(request):
	car_uuid = request.GET.get('id', None)
	cars = CarInstance.objects.all()
	for car in cars:
		print(car.uuid)
	car_qrs = CarInstance.objects.filter(uuid=car_uuid)
	return render(request, 'car_info.html', {'user_id': request.user, 'car': car_qrs})

@login_required
def account(request): #This one surely must login.
	user_qrs = list(User.objects.filter(username=request.user))
	user_qrs = user_qrs[0]

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

	return render(request, "registration/account.html", {
		'form': form,
		'car_form': car_form,
		'car_instances': car_instances,
		'user_details': user_qrs, 
		'user_id': request.user,
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

def rent(request): #This is the processor for renting the car itself. For this, user MUST be logged in.
	#there should be some query and stuff.
	query_string = ''
	if (request.user.is_authenticated()) :
		#do some renting logic here!
		return redirect('/accounts/user')
	else :
		return redirect('/rent/auth?next=/rent/' + query_string)
	

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

	print(request.GET)
	change_email_form = changeEmailForm(request.GET)
	change_user_details_form = changeUserDetailsForm(request.GET)

	if (change_email_form.is_valid()):
		new_email = (dict(change_email_form.cleaned_data))['email']
		if (new_email):
			user_qrs.email = new_email
			user_qrs.save()

	if (change_user_details_form.is_valid()):
		contact = (dict(change_user_details_form.cleaned_data))['contact']
		address = (dict(change_user_details_form.cleaned_data))['address']
		print("contact = " + str(contact))
		print("address = " + str(address))
		if (contact):
			user_qrs.userdetails.contact = contact
			flag = True

		if (address):
			user_qrs.userdetails.address = address
			flag = True

		if (flag):
			user_qrs.userdetails.save()


	return redirect("/accounts/user")
