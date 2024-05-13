from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Post(models.Model):
    
    sno = models.AutoField(auto_created = True,primary_key = True)
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    author = models.CharField(max_length=70, null=False, blank=False)
    slug = models.CharField(max_length=130, null=False, blank=False)
    timestamp = models.DateTimeField(null=False, blank=False)

    def __str__(self):
     return self.title + "by" + self.author


class BlogComment(models.Model):
    sno = models.AutoField(auto_created = True,primary_key = True)
    comment = models.TextField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, null=False, blank=False)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)
    
    def __str__(self):
     return self.comment[0:13] 