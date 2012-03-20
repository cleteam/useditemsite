from django.db                  import models

class UserRole(models.Model):
    name        = models.CharField(max_length=50)
    active      = models.BooleanField(default=True)
    created_by  = models.IntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_by  = models.IntegerField()
    updated_at  = models.DateTimeField(auto_now_add=True)
          
class User(models.Model):    
    user_role   = models.ForeignKey(UserRole)
    user_type   = models.IntegerField()
    first_name  = models.CharField(50)
    last_name   = models.CharField(50)
    address     = models.CharField(150)
    email       = models.EmailField()
    phone       = models.CharField(20)
    gender      = models.BooleanField(default=True)
    birthday    = models.DateField()
    password    = models.CharField(30)
    active      = models.BooleanField(default=False)
    password_reseted    = models.BooleanField(default=True)
    last_login_at       = models.DateTimeField()
    created_by  = models.IntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_by  = models.IntegerField()
    updated_at  = models.DateTimeField(auto_now_add=True)    