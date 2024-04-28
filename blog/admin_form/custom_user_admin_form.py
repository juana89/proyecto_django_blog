from  django import forms
from django.contrib.auth.models import User
from ..models import CustomUser

class CustomUserAdminForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name =forms.CharField(required=False,label="Nombre")
    last_name =forms.CharField(required=False,label="Apellido")
    password = forms.CharField(
        widget= forms.PasswordInput(),required=False,label="Contraseña"
    )
    
    class Meta:
        model =CustomUser
        fields = ['avatar','dob','bio','github']
  #configuracion para actualizar los campos de user      
    def __init__(self,*args,**kwargs):
        super(CustomUserAdminForm,self).__init__(*args,**kwargs)
        if self.instance and self.instance.pk:
            self.fields['username'].initial = self.instance.user.username
            self.fields['email'].initial = self.instance.user.email
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            
    def save(self,commit=True):
        custom_user = super(CustomUserAdminForm,self).save(commit=False)
        
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        password =  self.cleaned_data['password']
        
        if self.instance.pk:#verifica si es actualizacion 
            user = self.instance.user 
            if user.username !=username:
                
              if User.objects.filter(username).exists():#comprueba si el usuario ya existe.
                 self.add_error('username','El nombre de uauario ya existe')
                 return None
              else:
                user.username =username
                
            if user.email != email:
                 if User.objects.filter(email).exists():#comprueba si el usuario ya existe.
                    self.add_error('email','El email ya existe')
                 return None
            else:
                user.email = email
             
            user.first_name =first_name
            user.last_name = last_name
        
            if password != "":
              user.set_password(password)
              user.save()
        
            if commit:
              custom_user.save()
            return custom_user
        
        else: #usuario nuevo
            if User.objects.filter(username=username).exists():#comprueba si el usuario ya existe.
                 self.add_error('username','El nombre de uauario ya existe')
                 return User.objects.filter(username=username).first()
            else:
                user =User.objects.create_user(
                    username = username,
                    email =email,
                    first_name =first_name,
                    last_name =last_name,
                )
                user.set_password(password)
                user.save()
                
                custom_user.user = user
                if commit:
                     custom_user.save()
                return custom_user
                
        
        