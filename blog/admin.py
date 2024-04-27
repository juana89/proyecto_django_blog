from django.contrib import admin
from .models import Post ,Category,Comment
from .models_user.custom_user import CustomUser
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','description','created_at',"image")
    search_fields = ('title',' description')
    exclude = ('updated_at','categories',' slug','comments_count ','views_count ','like_count')
    
@admin.register(CustomUser)
class  CustomUserAdmin(admin.ModelAdmin):
    list_display = ("user","fecha_nac","bio","github")
    exclude =("fecha_nac","bio","github")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description','slug')
    exclude =('slug',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
 list_display =('author','content','created_at') 
 

 
