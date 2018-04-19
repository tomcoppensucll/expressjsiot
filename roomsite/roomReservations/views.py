from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'roomReservations/index.html')

# Create your views here.
