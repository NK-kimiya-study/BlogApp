from django.contrib import admin

# Register your models here.
from .models import CustomUser,Post,Category,Group

class CustomUsderAdmin(admin.ModelAdmin):
    list_display = ('id','username')
    list_display_links = ('id','username')
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

class GroupAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')


admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Group,GroupAdmin)
