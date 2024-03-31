from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.decorators import login_required
from .models import Car, Driver, Reservation, ApprovedReservation
from .forms import CarForm, DriverForm, ReservationForm, ApprovedReservationForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def homepage(request):
    return render(request,"home/homepage.html")

def login_view(request):
    if request.method == "GET":
        return render(request, 'authentication/loginpage.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'authentication/loginpage.html',{'form':AuthenticationForm(), 'error':'Username and Password did not match'})
        else:
            login(request, user)
            if request.POST['username'] == 'admin':
                messages.success(request, "Administrator Logged In Successfully")
                return redirect('administrator')
            else:
                messages.success(request, "User Logged In Successfully")
                return redirect('user')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been successfully logged out!')
        return redirect('login')

def register_view(request):
    if request.method == "GET":
        return render(request, 'authentication/registerpage.html', {'form':UserCreationForm()})
    else:
        try:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                    user.save()
                    login(request, user)
                    messages.success(request, "Account Create Successfully!")
                    return redirect('user')
                except IntegrityError :
                    return render(request, 'authentication/registerpage.html', {'form':UserCreationForm(),'error':'Username is already taken'})                    
            else:
                return render(request, 'authentication/registerpage.html', {'form':UserCreationForm(),'error':'passwords did not match'})
        except ValueError:
            return render(request, 'authentication/registerpage.html', {'form':UserCreationForm(),'error':'Invalid Input'})  

def carinventory_view(request):
    cars = Car.objects.all().order_by("-id")
    return render(request, "administrator/car_inventory.html", {"cars":cars})

def aboutsystem_view(request):
    return render(request, "administrator/about_system.html")

@login_required
def addcar_view(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car_inventory')  # Redirect to car list view after successful form submission
    else:
        form = CarForm()
    return render(request, "administrator/add_car.html", {'form': form})



def editcar_view(request, car_id):
    # Retrieve the car object or return a 404 error if it doesn't exist
    car = get_object_or_404(Car, pk=car_id)
    
    if request.method == 'POST':
        # If it's a POST request, process the form data
        form = CarForm(request.POST, request.FILES,instance=car)
        if form.is_valid():
            # If form data is valid, save changes to the database
            form.save()
            messages.success(request, 'Car successfully Edited')
            return redirect('car_inventory')  # Assuming 'car_inventory' is the name of your car inventory page URL
    else:
        # If it's a GET request, create a form pre-filled with the car's data
        form = CarForm(instance=car)
    
    # Pass the form to the template for rendering
    return render(request, 'administrator/edit_car.html', {'form': form, 'car': car})

def deletecar_view(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        # If the request method is POST, delete the car object
        
        car.delete()

        messages.success(request, 'Car successfully deleted')
        # Redirect to the desired URL after deletion
        return redirect('car_inventory')
    else:
        # If the request method is not POST, render a template with a confirmation form
        return render(request, 'administrator/car_inventory.html')

@login_required
def reservecar_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user  # Associate the currently logged-in user
            reservation.save()
            messages.success(request, 'Your Request Is Being Evaluated. Please wait until we review your Reservation, Thank you!')
            return redirect('user')  # Redirect to a success page or any other page
    else:
        form = ReservationForm()
    return render(request, "user/reserve_car.html", {'form': form})

def driverinventory_view(request):
    drivers = Driver.objects.all().order_by("-id")
    return render(request, "administrator/driver_inventory.html", {"drivers":drivers})

def add_driver_view(request):
    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Driver successfully added')
            return redirect('driver_inventory')  # Redirect to car list view after successful form submission
    else:
        form = DriverForm()
    return render(request, "administrator/add_driver.html", {'form': form})



def editdriver_view(request, driver_id):
    # Retrieve the car object or return a 404 error if it doesn't exist
    driver = get_object_or_404(Driver, pk=driver_id)
    
    if request.method == 'POST':
        # If it's a POST request, process the form data
        form = DriverForm(request.POST, request.FILES,instance=driver)
        if form.is_valid():
            # If form data is valid, save changes to the database
            form.save()
            messages.success(request, "Driver Information Edited Successfully")
            return redirect('driver_inventory')  # Assuming 'car_inventory' is the name of your car inventory page URL
    else:
        # If it's a GET request, create a form pre-filled with the car's data
        form = DriverForm(instance=driver)
    
    # Pass the form to the template for rendering
    return render(request, 'administrator/edit_driver.html', {'form': form, 'driver': driver})

def deletedriver_view(request, driver_id):
    driver = get_object_or_404(Driver, pk=driver_id)
    if request.method == 'POST':
        # If the request method is POST, delete the car object
        driver.delete()
        messages.success(request, 'Driver successfully deleted')
        # Redirect to the desired URL after deletion
        return redirect('driver_inventory')
    else:
        # If the request method is not POST, render a template with a confirmation form
        return render(request, 'administrator/driver_inventory.html')

def reservations_view(request):
    reservations = Reservation.objects.filter(is_approved=False).order_by("-id")
    return render(request, "administrator/reservations.html", {"reservations":reservations})


def del_reservation_view(request, res_id):
    reservation = get_object_or_404(Reservation, pk=res_id)
    if request.method == 'POST':
        # If the request method is POST, delete the car object
        reservation.delete()
        messages.success(request, 'Reservation successfully deleted')
        # Redirect to the desired URL after deletion
        return redirect('reservations')
    else:
        # If the request method is not POST, render a template with a confirmation form
        return render(request, 'administrator/reservations.html')


@login_required
def administrator_view(request):
    return render(request, 'administrator/administrator_dashboard.html')

@login_required
def user_view(request):
    return render(request, 'user/user.html')


def approve_reservation_view(request, res_id):
    reservation = get_object_or_404(Reservation, pk=res_id)

    if request.method == 'POST':
        # If it's a POST request, process the form data
        form = ApprovedReservationForm(request.POST, request.FILES)
        if form.is_valid():
            # If form data is valid, save changes to the database
            form.save()
            reservation.is_approved = True  # Set is_approved to True
            reservation.save()
            messages.success(request, "Reservation Has Been Approved")
            return redirect('reservations')  # Assuming 'car_inventory' is the name of your car inventory page URL
    else:
        # If it's a GET request, create a form pre-filled with the car's data
        form = ApprovedReservationForm()
    
    # Pass the form to the template for rendering
    return render(request, 'administrator/approve_reservation.html', {'form': form, 'reservation': reservation})

def approved_requests_view(request):
    approved_reservations = ApprovedReservation.objects.all().order_by("-id")

    per_page = 7

    paginator = Paginator(approved_reservations, per_page)

    page_number = request.GET.get('page')
    try:
        approved_reservations = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        approved_reservations = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        approved_reservations = paginator.page(paginator.num_pages)

    return render(request, "administrator/approved_requests.html", {'approved_reservations':approved_reservations})
