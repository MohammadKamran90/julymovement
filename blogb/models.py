from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.



class Post(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset(). filter(status='published')
        
    options ={
        ('draft', 'Draft',),
        ('published', 'Published',),
        
    }

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    excerpt = models.TextField(null=True)
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, choices= options, default= 'draft')
    objects = models.Manager()
    newmanager = NewManager()



    def get_absolute_url(self):
        return reverse('blogb:single_post', args=[self.slug])

    class Meta: 
        ordering = ('publish',)

    def __str__(self):
        return self.title
    

