"""albert_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from app01.views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/',include('ckeditor_uploader.urls')),
    url(r'^index/',index),
]
urlpatterns += [
    url(r'^base/', base),
    url(r'^aboutMe/',aboutMe),
    url(r'^myArticle/',myArticle),
    url(r'^mypicture/',myPicture),
    url(r'^article/',Article_source)
]

urlpatterns += [
    url(r'^vuetest/',vuetest),
    url(r'^vue/',vue),  # 文章分页
    url(r'^vuesource/',vuesource),
]
