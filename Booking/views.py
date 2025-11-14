from django.shortcuts import render

# Create your views here.
from Booking.models import *
from django.http import HttpResponse
def insert_movie(request):
    name = input('Enter the movie name')
    genre = input("Enter the genre")
    duration = float(input('Enter the duration(in hours)'))
    TMO = Movie.objects.get_or_create(title = name, genre = genre,duration= duration)
    if TMO[1]:
        return HttpResponse('Record created')
    else:
        return HttpResponse('Already Present')

def insert_booking(request):
    name = input('Enter the movie name')
    MO = Movie.objects.get(title = name)
    seat = int(input('Enter the seat number'))
    price = float(input('Enter price'))
    custname = input('Enter the name of customer')
    TBO = Ticket.objects.get_or_create(title = MO,seat_number = seat,price =price,c_name = custname)
    if TBO[1]:
        return HttpResponse('Record added')
    else:
        return HttpResponse('Already booked')