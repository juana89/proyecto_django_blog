from django.contrib import admin
from blog.models import Post ,Category,Comment
# Register your models here.


admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','description','created_at','image ')
    search_fields = ('title',' description')
    

admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =('name','descripcion','slug')
    exclude =('slug')
    
admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
 list_display =('author','description','create_at') 
 

 
