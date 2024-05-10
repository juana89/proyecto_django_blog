from django.urls import path
from blog.views import *

urlpatterns = [
    path('',home,name="home"),
    path('signin/',signin,name="signin"),
    path('logout/',logout_view,name="logout"),
    path("post/<int:post_id>/", post_detail, name="post_detail"),
    path('categorie/',categorie_views,name="categorie"),
    path('create/',create_post,name="create"),
    path('search/',search_post,name="search_post"),
    
]
