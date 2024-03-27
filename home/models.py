from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    plate_number = models.CharField(max_length=17, unique=True)
    mileage = models.DecimalField(max_digits=10, decimal_places=2)
    engine_size = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    car_picture = models.ImageField(upload_to='cars/', blank=True, null=True,default='cars/default-img.jpg')


    def __str__(self):
        return (
            f"{self.make} "
            f"{self.model} "
            f"{self.plate_number}: "  # Include %Z to display timezone name
        )
    
class Driver(models.Model):
    driver_name = models.CharField(max_length=100)
    license_number = models.CharField(unique=False,max_length=100)
    contact_number = models.IntegerField()
    driver_status = models.CharField(max_length=50)
    driver_picture = models.ImageField(upload_to='drivers/', blank=True, null=True, default='drivers/default-driver.jpeg')

    def __str__(self):
        return (
            f"{self.driver_name} "
            f"{self.contact_number} "
        )
    
class Reservation(models.Model):
    requestor_name = models.CharField(max_length=100)
    office_department_college = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    appointment_status = models.CharField(max_length=50)
    requestor_address = models.CharField(blank=True,max_length=100)
    number_of_passengers = models.IntegerField()
    destination = models.CharField(max_length=50)
    date_of_travel = models.DateField(null=True, blank=True)
    purpose_of_travel = models.CharField(blank=True,max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"{self.requestor_name} |"
            f"{self.contact_number} "
        )
    
    
    
    
