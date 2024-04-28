from django.shortcuts import render
from .models import Post

from .models_user import *
def home (request):
   post_cant = Post.objects.filter(status="publicado").count()
   post_recientes = Post.objects.filter(status="publicado").order_by("created_at")[:3]
   post_mas_vistos =Post.objects.filter(status="publicado").order_by("views_count")[:3]
     
   context ={
    "post_recientes" :post_recientes,
     "cantidad_post" :post_cant,
     "post_reciente" : post_mas_vistos
        }
   return render(request,'blog/home.html',context)
    