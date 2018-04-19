from django.shortcuts import render, HttpResponse
from .models import Roomstatus
import operator



def index(request):
    query_unsortedRooms =  Roomstatus.objects.all()
    query_rooms  = sorted(query_unsortedRooms, key = operator.attrgetter('lokaal'))
    return render(request, 'roomReservations/index.html', context = {'query_rooms':query_rooms})
	


# Create your views here.
