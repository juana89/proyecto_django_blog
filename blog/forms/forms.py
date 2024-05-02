from django.forms import ModelForm
from models import Post

class CreateForm(ModelForm):
    class meta:
        model : Post
        field ="__all__"