from django import forms            
from django.contrib.auth.models import User   # fill in custom user info then save it 
from models import UserDetails
from django.contrib.auth.forms import UserCreationForm      

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
    dob = forms.DateField(label="Date of birth (dd/mm/yyyy)", required=True, widget=forms.DateInput(format='%d/%m/%Y'))
    contact = forms.CharField(required=True, min_length=8)
    license_issue_date = forms.DateField(label="License issue date (dd/mm/yyyy)", required=True, widget=forms.DateInput(format='%d/%m/%Y'))
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