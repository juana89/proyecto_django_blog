from  django import forms
from django.contrib.auth.models import User
from ..models import CustomUser

class CustomUserAdminForm(forms.ModelForm):
    user = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name =forms.CharField(required=False,label="Nombre")
    last_name =forms.CharField(required=False,label="Apellido")
    password = forms.CharField(
        widget= forms.PasswordInput(),required=True,label="Contraseña"
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
    