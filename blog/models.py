from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
from .models_user.custom_user_models import CustomUser
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    color=models.CharField(max_length=20)   
    
    def __str__(self):
         return self.name
     
    def save (self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args,**kwargs)
        
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    content =HTMLField(default="")
    description = models.CharField(max_length=100,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    status =  models.CharField(
        max_length=20,
        choices=[
            ("borrador", "Borrador"),
            ("publicado", "Publicado"),
            ("eliminado", "Eliminado"),
        ],
    default ="publicado",
    blank=True,         
    )
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='blog/post',default='blog/post/default.png',blank=True)
    comments_count = models.IntegerField(default =0)
    views_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    def save (self,*args,**kwargs):
        if not self.image:
            self.image = "blog/post/default.png"
            self.slug = slugify(self.title)
        super(Post,self).save(*args,**kwargs)
        
class  PostCategory(models.Model):
    post =models.ForeignKey(Post, on_delete=models.CASCADE)
    category =models.ForeignKey(Category,on_delete=models.CASCADE)
     
     
class Comment (models.Model):
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    content = models.TextField()
    created_at =models.DateTimeField()
    updated_at = models.DateTimeField( )
    post =models.ForeignKey(Post, on_delete=models.CASCADE)
    likes_count =models.IntegerField()
    
    
