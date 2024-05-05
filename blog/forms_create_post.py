from django.forms import *
from .models import Post

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
                    "class":"form-control post-f",
                }
            ),
            "author":TextInput(
                attrs={
                    "placeholder":"Ingrese su nombre",
                    "class":"form-control",
                }
            ),
            
            "content":Textarea(
                attrs={
                    "placeholder":"Ingrese el contenido",
                    "class":"form-control",
                }
            ),
            "image":FileInput(
                attrs={
                    "class":"form-control file"
                }
            )
            
        }
        
        