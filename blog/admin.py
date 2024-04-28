from django.contrib import admin
from .models import Post ,Category,Comment
from .models_user.custom_user_models import CustomUser
# Register your models here.
from .admin_form.custom_user_admin_form import CustomUserAdminForm

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','content','description','created_at','image','status','slug','views_count','like_count')
    search_fields = ('title',' description')
    exclude = ('updated_at','categories',' slug','comments_count ','views_count ','like_count')
    
  
@admin.register(CustomUser)
class  CustomUserAdmin(admin.ModelAdmin):
    form = CustomUserAdminForm
    def get_form(self,request,obj =None,**kwargs):
        form = super().get_form(request,obj,**kwargs)
        
        form.base_fields =dict(
            [
                ('username',form.base_fields['username']),
                ('email',form.base_fields['email']),
                ('first_name',form.base_fields['first_name']),
                ('last_name',form.base_fields['last_name']),
                ('password',form.base_fields['password']),
                ('avatar',form.base_fields['avatar']),
                ('dob',form.base_fields['dob']),
                ('bio',form.base_fields['bio']),
                ('github',form.base_fields['github']),
            ]
            + list(form.base_fields.items())
        )
        return form
    
    list_display = ('get_username','get_email','dob','github','get_bio')
    
    def get_username(self,obj):
        return obj.user.username if obj.user else None
    
    get_username.short_description = 'Usuario'
    
    def get_email (self,obj):
       return obj.user.email if obj.user else None
   
    get_email.short_description = 'Email'
    def get_bio(self,obj):
        return obj.bio if obj.bio else 'Sin biografia'
    
    get_username.short_description = 'Biografia'
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description','slug')
    exclude =('slug',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
 list_display =('author','content','created_at') 
 

 
