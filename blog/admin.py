from multiprocessing import Event
from django.contrib import admin
from blog.models import Blog    
from blog.models import Contact

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {
        
        "all" : ("/blog/static/css/main.css",)
        
        }

        js = ("/blog/static/js/blog.js",)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact)

