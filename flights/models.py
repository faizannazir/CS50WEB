from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code}) "


class Flight(models.Model):
    # origin = models.CharField(max_length=64)    
    # destination = models.CharField(max_length=64)
    origin= models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination= models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return(f"{self.id} {self.origin} to {self.destination} takes {self.duration} minutes")


#  Shell 
# >>> from flights.models import *
# >>> lhr = Airport.objects.create(code="LHR",city="Lahore") 
# >>> lhr.save()
# >>> khr = Airport.objects.create(code="KHR",city="Karachi") 
# >>> khr.save()
# >>> isl = Airport.objects.create(code="ISL",city="Islamabad") 
# >>> isl.save()
# >>> f1 = Flight(origin = lhr , destination = isl,duration=120)
# >>> f1.save()
# >>> f2 = Flight(origin = isl, destination = khr,duration=120)  
# >>> f2.save() 
# >>> f3 = Flight(origin = khr, destination = lhr,duration=250) 
# >>> f3.save()
# 
# >>> f2.duration
# 120
# 
# >>> f2.duration =190
# >>> f2.duration      
# 190
# 
# >>> f1
# <Flight: 1 Lahore (LHR)  to Islamabad (ISL)  takes 120 minutes>
# >>> f1.origin
# 
# <Airport: Lahore (LHR) >
# >>> f1.destination
# <Airport: Islamabad (ISL) >
# 
# >>> f1.origin.city 
# 'Lahore'
# >>> f1.origin.code 
# 'LHR'
# 
# >>> lhr.arrivals.all()
# <QuerySet [<Flight: 3 Karachi (KHR)  to Lahore (LHR)  takes 250 minutes>]>
# 
# >>> lhr.departures.all() 
# <QuerySet [<Flight: 1 Lahore (LHR)  to Islamabad (ISL)  takes 120 minutes>]>
#