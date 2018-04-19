from django.shortcuts import render, HttpResponse
from .models import Roomstatus



def index(request):
    query_rooms =  Roomstatus.objects.all()
    return render(request, 'roomReservations/index.html', context = {'query_rooms':query_rooms})
	


# Create your views here.
