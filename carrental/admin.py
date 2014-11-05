from django.contrib import admin
from models import Car, CarInstance, Booking, UserDetails

class CarAdmin(admin.ModelAdmin):
    list_display = ('make_model', 'max_passengers', 
                    'transmission', 'aircon', 'type')

class CarInstanceAdmin(admin.ModelAdmin):
    list_display = ('make_model', 'colour', 'owner', 'price',
                    'can_drive_to_malaysia', 'year', 'carplate')
    
    def make_model(self, instance):
        return instance.car.make_model
    
    def can_drive_to_malaysia(self, instance):
        return instance.candrivemy

class BookingAdmin(admin.ModelAdmin):
    list_display = ('start', 'end', 'car_instance', 'borrower')

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'nric', 'dob', 'contact',
                    'license_issue_date', 'address')

admin.site.register(Car, CarAdmin)
admin.site.register(CarInstance, CarInstanceAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(UserDetails, UserDetailsAdmin)