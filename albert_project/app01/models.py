from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

#作者

class Author(models.Model):
    gender_choice = (
        ("M","Male"),
        ("F","Female")
    )
    name = models.CharField(verbose_name="作者姓名",max_length=32,blank=True,null=True)
    age = models.CharField(verbose_name="作者年龄",blank=True,null=True,max_length=3)
    gender = models.CharField(max_length=2,choices=gender_choice,verbose_name="作者性别",blank=True,null=True)
    email = models.CharField(verbose_name="作者邮箱",blank=True,null=True,max_length=32)
    phone = models.CharField(max_length=11,verbose_name="作者电话",null=True,blank=True)
    photo = models.ImageField(upload_to="images/author",verbose_name="作者头像")


    def __str__(self):
        return "作者：%s"%self.name
#标签
class Classify(models.Model):
    label = models.CharField(max_length=32,verbose_name="分类标签")
    description = models.TextField(verbose_name="标签描述")

    def __str__(self):
        return "标签：%s"%self.label

#评论

class Comment(models.Model):
    content = RichTextUploadingField(verbose_name="评论内容")
    content_name = models.CharField(max_length=32,verbose_name="评论用户")
    time = models.DateTimeField(verbose_name="评论时间")
    agree = models.IntegerField(verbose_name="评论点赞") # 点赞功能
    def __str__(self):
        return "[%s]评论：%s"%(self.content_name,self.content)

#图片
class Picture(models.Model):
    label = models.CharField(max_length=32,verbose_name="图片标签")
    image = models.ImageField(upload_to="images/picture",verbose_name="图片链接")
    description = RichTextUploadingField(verbose_name="图片描述")
    classify = models.ForeignKey(to=Classify,verbose_name="图片分类")
    comment = models.ForeignKey(to=Comment,verbose_name="图片评论")

    def __str__(self):
        return "图片名称：%s"%self.label

#文章
class Article(models.Model):
    title = models.CharField(max_length=32,verbose_name="文章标题")
    time = models.DateTimeField(verbose_name="发表日期")
    description = RichTextUploadingField(verbose_name="文章描述")
    content= RichTextUploadingField(verbose_name="文章内容")
    picture = models.ImageField(verbose_name="文章图片",upload_to="images/article")
    clssify = models.ForeignKey(Classify)
    author = models.ForeignKey(Author)
    comment = models.ForeignKey(to=Comment,verbose_name="文章评论",blank=True,null=True)
    def __str__(self):

        return  "文章标题：%s"%self.title