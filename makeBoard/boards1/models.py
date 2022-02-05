from django.db import models

# Create your models here.


from django.contrib.auth.models import User

#http 상태를 나타내기 위한 장고 모듈

from ckeditor.fields import RichTextField

class Topic(models.Model):
    message = models.TextField(max_length=5000,null=True)
    subject = models.CharField(max_length=255)
    last_updated =  models.DateField(auto_now_add=True, null=True)
    writter = models.ForeignKey(User, related_name='topics',on_delete=models.CASCADE, null=True)    

class Reply(models.Model):
    message = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by= models.ForeignKey(User, null=True, related_name='posts',on_delete=models.CASCADE)
    updated_at = models.DateField(null = True)
    updated_by=  models.ForeignKey(User,null=True,related_name='+',on_delete=models.CASCADE)