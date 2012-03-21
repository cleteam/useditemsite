from django.db                  import models
from apps.account.models        import User

class City(models.Model):
    name        = models.CharField(max_length=50)
    active      = models.BooleanField(default=True)
    created_by  = models.IntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_by  = models.IntegerField()
    updated_at  = models.DateTimeField(auto_now_add=True)
    
class District(models.Model):
    city        = models.ForeignKey(City)
    name        = models.CharField(max_length=50)
    active      = models.BooleanField(default=True)
    created_by  = models.IntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_by  = models.IntegerField()
    updated_at  = models.DateTimeField(auto_now_add=True)    
    
class UsedItem(models.Model):
    user        = models.ForeignKey(User)
    title       = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    image       = models.ImageField(upload_to="events/%Y/%m/%d")
    note        = models.CharField(max_length=200, null=True)
    state       = models.IntegerField()
    active      = models.BooleanField(default=True)
    address     = models.CharField(max_length=150)
    district    = models.ForeignKey(District)
    city        = models.ForeignKey(City)
    phone       = models.CharField(max_length=20, null=True)
    created_by  = models.IntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_by  = models.IntegerField()
    updated_at  = models.DateTimeField(auto_now_add=True)

class Recipient(models.Model):
    useditem    = models.ForeignKey(UsedItem)
    user        = models.ForeignKey(User)
    accepted    = models.BooleanField(default=False)
    created_by  = models.IntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_by  = models.IntegerField()
    updated_at  = models.DateTimeField(auto_now_add=True)    