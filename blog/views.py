from django.shortcuts import render,redirect
from .models import Post,Category
from django.contrib.auth.decorators import login_required
from .models_user import *
from  .forms_create_post import CreateForm

#sentencia para inicar y cerrar sesion
from  django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login, logout

#Dependencia para consultas complejas
from django.db.models import Q
from. models import Post,Comment

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
  
#------------------------
def search_post(request):
   search=request.GET.get("search", "") 
   if search:
      post =Post.objects.filter(
         Q(title__icontains=search)|
         Q(content__icontains=search),
         status="publicado",
      ).distinct()
   else:     
      post =Post.objects.none()
   return render(request,'blog/search.html',{'post':post,'search':search})
   
def post_detail(request,post_id):
   post=Post.objects.get(id=post_id)
   return render(request,"blog/post_detail.html",{'post':post})
#_____________________-
def categorie_views(request):
   return render(request,"blog/categoria.html")


def create_post(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateForm()
    return render(request, 'blog/create_post_form.html', {'form': form})



