from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from elugan import settings

urlpatterns = [
    path('', views.homepage, name="home"),

    #Authentication
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.register_view, name="register"),

    #Landing Pages
    path('administrator', views.administrator_view, name="administrator"),
    path('user', views.user_view, name="user"),

    #Inventories
    path('car_inventory', views.carinventory_view, name="car_inventory"),
    path('driver_inventory', views.driverinventory_view, name="driver_inventory"),

    #Other Pages
    path('about', views.aboutsystem_view, name="about"),

    #Car CRUD
    path('add_car', views.addcar_view, name="add_car"),
    path('edit_car/<int:car_id>', views.editcar_view, name="edit_car"),
    path('del_car/<int:car_id>', views.deletecar_view, name="del_car"),
    path('edit_car/car_inventory', views.carinventory_view),

    #Reserve Car
    path('reserve_car', views.reservecar_view, name="reserve_car"),
    path('reservations', views.reservations_view, name="reservations"),
    path('del_reservation/<int:res_id>', views.del_reservation_view, name="del_reservation"),


    #Driver CRUD
    path('add_driver', views.add_driver_view, name="add_driver"),
    path('edit_driver/<int:driver_id>', views.editdriver_view, name="edit_driver"),
    path('del_driver/<int:driver_id>', views.deletedriver_view, name="del_driver"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)