from django import forms            
from django.contrib.auth.models import User   # fill in custom user info then save it 
from models import UserDetails, CarInstance, Car, TYPE_CHOICES, TRANSMISSION_CHOICES
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelChoiceField
from django.forms.extras.widgets import *


class CustomRegistrationForm(UserCreationForm):
    #email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self,commit=True):   
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class UserDetailsForm(forms.ModelForm):
    nric = forms.CharField(required=True, min_length=9)
    dob = forms.DateField(label="Date of birth (dd/mm/yyyy)", required=True, input_formats=['%d/%m/%Y'], widget=forms.DateInput(format='%d/%m/%Y'))
    contact = forms.CharField(required=True, min_length=8)
    license_issue_date = forms.DateField(label="License issue date (dd/mm/yyyy)", input_formats=['%d/%m/%Y'], required=True, widget=forms.DateInput(format='%d/%m/%Y'))
    address = forms.CharField(required=True)

    class Meta:
        model = UserDetails
        exclude = ('user',)
        fields = ('nric', 'dob', 'contact', 'license_issue_date', 'address')

    def save(self,commit=True):   
        user_details = super(UserDetailsForm, self).save(commit=False)
        user_details.nric = self.cleaned_data['nric']

        if commit:
            user_details.save()

        return user_details



class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return str(obj.make_model)


class SelectCarForm(forms.Form):
    car = MyModelChoiceField(queryset=Car.objects.all(), to_field_name="make_model")


class changeEmailForm(forms.Form):
    email = forms.EmailField()


class changeUserDetailsForm(forms.Form):
    contact = forms.CharField(max_length=8, required=False)
    address = forms.CharField(max_length=512, required=False)


class AddCarInstanceForm(forms.ModelForm):
    colour = forms.CharField(required=True, max_length=128)
    price = forms.DecimalField(required=True, decimal_places=2, max_digits=10)
    candrivemy = forms.BooleanField(required=False)
    carplate = forms.CharField(required=True, max_length=16)
    year = forms.IntegerField(required=True)

    class Meta:
        model = CarInstance
        exclude = ('car', 'owner')
        fields = ('colour', 'price', 'candrivemy', 'carplate')

    def save(self,commit=True):   
        car_instance = super(AddCarInstanceForm, self).save(commit=False)
        car_instance.colour = self.cleaned_data['colour']
        car_instance.price = self.cleaned_data['price']
        car_instance.candrivemy = self.cleaned_data['candrivemy']
        car_instance.carplate = self.cleaned_data['carplate']
        car_instance.year = self.cleaned_data['year']

        if commit:
            car_instance.save()

        return car_instance
    

class SearchCarForm(forms.Form):
    car = forms.CharField(max_length=64, required=False, label="Make/model")
    price_lower = forms.DecimalField(decimal_places=2, max_digits=10, required=False, label="Price starting from")
    price_upper = forms.DecimalField(decimal_places=2, max_digits=10, required=False, label="to")
    passengers = forms.IntegerField(label="Number of passengers of at least", required=False)
    type = forms.CharField(required=False, max_length=2, widget=forms.Select(choices=TYPE_CHOICES))


class RentCarForm(forms.Form):
    carplate = forms.CharField(max_length=16, required=True)
    dateStart = forms.CharField(max_length=10, required=True)
    dateEnd = forms.CharField(max_length=10, required=True)

    
class MoreDetailedSearchCarForm(SearchCarForm):
    colour = forms.CharField(max_length=128, required=False)
    candrivemy = forms.NullBooleanField(required=False, label="Can drive to Malaysia", initial=None)
    year = forms.IntegerField(required=False)
    transmission = forms.CharField(required=False, max_length=2, widget=forms.Select(choices=TRANSMISSION_CHOICES))
    aircon = forms.NullBooleanField(required=False, label="Got aircon", initial=None)
    ordering = forms.CharField(required=False, max_length=128)
    ascending = forms.NullBooleanField(required=False)