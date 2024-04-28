from django.contrib.auth.models import User
from django.db import models



class CustomUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/",null=True,blank=True)
    dob =models.DateField(null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    github = models.URLField(null=True,blank=True)
    _is_deleting =False
    
    def delate(self,*args,**kwargs):
        if not self._is_deleting:
            self._is_deleting =True
            try:
                super().delete(*args,**kwargs)
            finally:
                self._is_deleting =False
    
    def __str__(self):
        return self.user.username
                
