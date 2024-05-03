from django.urls import path
from blog.views import *

urlpatterns = [
    path('',home,name="home"),
    path('signin/',signin,name="signin"),
    path('logout/',logout_view,name="logout"),
    path('post/',post_views,name="post"),
    path('categorie/',categorie_views,name="categorie"),
    path('create/',create_views,name="create"),
    
]
