from django.db                  import models
from apps.account.models        import User
from apps.main.models           import District, City

class Org(models.Model):
    name        = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image       = models.ImageField()
    address     = models.CharField(max_length=150)
    district    = models.ForeignKey(District)    
    city        = models.ForeignKey(City)
    phone       = models.CharField(max_length=20, null=True)
    active      = models.BooleanField(default=False)
    created_by  = models.IntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_by  = models.IntegerField()
    updated_at  = models.DateTimeField(auto_now_add=True)    

class Post(models.Model):
    user        = models.ForeignKey(User)
    title       = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    image       = models.ImageField()
    org         = models.ForeignKey(Org)
    active      = models.BooleanField(default=True)
    created_by  = models.IntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_by  = models.IntegerField()
    updated_at  = models.DateTimeField(auto_now_add=True)        