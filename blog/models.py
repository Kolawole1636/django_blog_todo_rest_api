from email.policy import default
from django.db import models
from django.contrib.auth.models import User



# Create your models here.

STATUS =(
    ('draft','Draft'),
    ('publish','Published')
)

class Blog(models.Model):

    class Newmanager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='publish')

    title = models.CharField(max_length=200,default='My blog')
    desc = models.TextField(default='This is my blog')
    img = models.ImageField(upload_to ='media/image',default='static/kola2.jpg', blank = True,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    created_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=12,choices=STATUS,default='publish')
    objects= models.Manager()

    newmanager = Newmanager()

    class Meta:
        ordering =('-created_on',)

    def __str__(self):
        return self.title    

    @property
    def urlImage(self):
        try:
            url=self.img.url

        except:
            url=''
        return url








