from django.contrib import admin

# Register your models here.
from Booking.models import *
admin.site.register(Movie)
admin.site.register(Ticket)