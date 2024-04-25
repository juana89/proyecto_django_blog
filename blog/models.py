from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models. CharField(max_length=255)
    slug = models.SlugField(unique=True)
    color=models.CharField(max_length=20)
    
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content =HTMLField()
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category')
    status =  models.CharField(
        max_length=20,
        choices=[
            ("borrador", "Borrador"),
            ("publicado", "Publicado"),
            ("eliminado", "Eliminado"),
        ],
    default =20,
    blank=True,
    )
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='blog',default='',blank=True)
    comments_count = models.IntegerField(default =0)
    views_count = models.IntegerField()
    like_count = models.IntegerField(default=0)

    
class  PostCategory(models.Model):
    post =models.ForeignKey(Post, on_delete=models.CASCADE)
    category =models.ForeignKey(Category,on_delete=models.CASCADE)

class Comment (models.Model):
    author =models.CharField(max_length=20)
    content = models.TextField()
    created_at =models.DateTimeField()
    updated_at = models.DateTimeField( )
    post =models.ForeignKey(Post, on_delete=models.CASCADE)
    likes_count =models.IntegerField()
    
    
