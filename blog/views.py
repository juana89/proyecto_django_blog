from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .models_user import *
from  .forms_create_post import CreateForm

#sentencia para inicar y cerrar sesion
from  django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login, logout

#Dependencia para consultas complejas
from django.db.models import Q
from. models import Post

@login_required
def home (request):
   post_cant = Post.objects.filter(status="publicado").count()
   post_recientes = Post.objects.filter(status="publicado").order_by("created_at")[:3]
   post_mas_vistos =Post.objects.filter(status="publicado").order_by("views_count")[:3]
     
  
   context ={
      "cantidad_post" :post_cant,
     "post_recientes" :post_recientes,
     "post_mas_visto" : post_mas_vistos,
        }
   return render(request,'blog/home.html',context)
    
def signin(request):
   if request.user.is_authenticated:
      return HttpResponseRedirect(reverse("home"))
   
   if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       user = authenticate(request, username=username, password=password)
       if user is not None:
          login(request,user)
          return redirect("home")
       else:
          return render(
             request,
             "blog/signin.html",
             {"error","invalido usuario o contraseña"},
          )
   else:#metodo GET
     return render(request,"blog/signin.html")
       
@login_required 
def  logout_view(request):
   logout(request)
   return HttpResponseRedirect(reverse("signin"))
  

def post_views(request):
  return render(request,'blog/post.html')

def categorie_views(request):
  return render(request,'blog/categoria.html')



def create_views(request):
      
    return render(request,'blog/create_form.html',{'form':CreateForm})
   
 #if  request.method =="POST":
 #    form = CreateForm(request.POST)
 #if form.is_valid():
 #       form.save()
 #else:
 #  form =CreateForm()
 #     
 #context ={'title':'titulo','form':form ,}
 #return render(request,'blog/create_form.html',context)