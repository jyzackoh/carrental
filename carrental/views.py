from forms import CustomRegistrationForm, UserDetailsForm, AddCarInstanceForm, SelectCarForm
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from models import CarInstance
from django import forms

def index(request):
	return render(request, 'index.html', {'user_id': request.user})

def search(request):
	query = request.GET.get('query', None)
	car_qrs = None
	if (query):
		car_qrs = CarInstance.objects.filter(car__make_model__contains=query)
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