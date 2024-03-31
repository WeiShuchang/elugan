from django import forms
from .models import Car, Driver, Reservation, ApprovedReservation


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'color', 'plate_number', 'mileage', 'engine_size', 'transmission', 'fuel_type','car_picture',]

        def clean_plate_number(self):
            plate_number = self.cleaned_data['plate_number']
            # Get the instance if it exists, None otherwise
            instance = getattr(self, 'instance', None)
            # If instance exists and the plate number hasn't changed, return the plate number
            if instance and instance.pk and instance.plate_number == plate_number:
                return plate_number
            # Check if the plate number already exists in the database
            if Car.objects.filter(plate_number=plate_number).exists():
                raise forms.ValidationError("Plate number already exists.")
            return plate_number
        
class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ['user']  
    

class ApprovedReservationForm(forms.ModelForm):
    def __init__(self, *args, exclude_unavailable=False, **kwargs):
        super(ApprovedReservationForm,self).__init__(*args, **kwargs)
        if exclude_unavailable:
            self.fields['driver'].queryset = Driver.objects.exclude(approvedreservation__isnull=False)
            self.fields['car'].queryset = Car.objects.exclude(approvedreservation__isnull=False)
        
    class Meta:
        model = ApprovedReservation
        fields = ['office_department_college', "requestor_address" ,'contact_number','appointment_status', 'driver', 'car', 'date_of_travel', 'expected_return_date', 'destination', 
                  'number_of_passengers', 'purpose_of_travel', 'requestor_name']