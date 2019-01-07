from django.contrib import admin
from app01.models import *

# Register your models here.
class Authoradmian(admin.ModelAdmin):
    list_display = ("name","age","email")
class Articleadmin(admin.ModelAdmin):
    # list_display = ("title","time","author")
    search_fields = ["title","time"] # 添加搜索选项
class Commentadmin(admin.ModelAdmin):
    list_display = ("content_name","time")
class pictureadmin(admin.ModelAdmin):
    list_display = ("label","classify")
class Classifyadmin(admin.ModelAdmin):
    list_display = ("label","description")
admin.site.register(Author,Authoradmian)
admin.site.register(Comment,Commentadmin)
admin.site.register(Classify,Classifyadmin)
admin.site.register(Article,Articleadmin)
admin.site.register(Picture,pictureadmin)
