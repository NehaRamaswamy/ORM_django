from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField()
    genre = models.CharField()
    duration = models.FloatField(help_text="Duration in hours") #Added help_text for readability

    def __str__(self):
        return self.title

class Ticket(models.Model):
    title = models.ForeignKey(Movie,on_delete = models.CASCADE)
    seat_number = models.CharField(max_length=10)    
    price = models.DecimalField(max_digits=6,decimal_places=2)
    c_name = models.CharField()