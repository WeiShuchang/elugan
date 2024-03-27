from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "authentication/loginpage.html")

def register(request):
    return render(request, "authentication/registerpage.html")