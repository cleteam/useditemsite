from django.db                  import models
from apps.account.models        import User
from apps.main.models           import District, City

class Event(models.Model):
    user        = models.ForeignKey(User)
    title       = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    started_at  = models.DateField()
    ended_at    = models.DateField()
    address     = models.CharField(max_length=150)
    district    = models.ForeignKey(District)    
    city        = models.ForeignKey(City)    
    active      = models.BooleanField(default=True)    
    created_by  = models.IntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_by  = models.IntegerField()
    updated_at  = models.DateTimeField(auto_now_add=True)        
    
class Enrollment(models.Model):
    user        = models.ForeignKey(User)
    event       = models.ForeignKey(Event)
    created_by  = models.IntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_by  = models.IntegerField()
    updated_at  = models.DateTimeField(auto_now_add=True)    