from forms import CustomRegistrationForm, UserDetailsForm, AddCarInstanceForm
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms

def index(request):
	return render(request, 'index.html', {'user_id': request.user})

def search(request):
	return render(request, 'search.html', {'user_id': request.user})

def car_info(request):
	return render(request, 'car_info.html', {'user_id': request.user})

@login_required
def account(request): #This one surely must login.
    user_qrs = list(User.objects.filter(username=request.user))
    user_qrs = user_qrs[0]

    if request.method == 'POST': #create new user
        form = AddCarInstanceForm(request.POST)
        if form.is_valid():
            car_instance = form.save(commit=False)
            car_instance.owner = user_qrs
            #car_instance.car = None
            car_instance.save()
            return HttpResponseRedirect("/accounts/user")
    else:
        form = AddCarInstanceForm()

    return render(request, "registration/account.html", {
        'form': form,
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
    #pass in owned cars
    #pass in rented cars
    return render(request, 'registration/account_public.html', {'valid':True, 'user_details': user_qrs, 'user_id': request.user})

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