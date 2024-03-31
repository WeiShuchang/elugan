# In your app's directory, create a new file e.g., context_processors.py
from .models import Reservation, ApprovedReservation  # Import your Reservation model

def reservation_count(request):
    num_approved_reservations = ApprovedReservation.objects.all().count()
    num_reservations = Reservation.objects.filter(is_approved=False).count()  # Get the count of reservations
    return {'num_reservations': num_reservations, 'num_approved_reservations':num_approved_reservations}
