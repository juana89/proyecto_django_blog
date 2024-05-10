from django.forms import *
from .models import Post
from  tinymce.widgets import TinyMCE
class CreateForm(ModelForm):
    class Meta:
        model = Post
        fields =['title','author','content','image']
        
        labels ={
            'title':'Titulo',
            'author':'Autor',
            'content':'Contenido',
            'image':'Imagen',            
        }
        widgets ={
            "title":TextInput(
                attrs={
                    "placeholder":"Ingrese el titulo",
                    "class":"form-control-sm",
                }
            ),
            "author":TextInput(
                attrs={
                    "placeholder":"Ingrese su nombre",
                    "class":"form-control-sm",
                }
            ),
            
            "content":TinyMCE(
                attrs={
                    "placeholder":"Ingrese el contenido",
                   
                }
            ),
            "image":FileInput(
                attrs={
                    "class":"form-control file"
                }
            )
            
        }
        
        