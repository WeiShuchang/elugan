from django.contrib import admin
from .models import Car, Driver, Reservation, ApprovedReservation

# Register your models here.
admin.site.register(Car)
admin.site.register(Driver)
admin.site.register(Reservation)
admin.site.register(ApprovedReservation)