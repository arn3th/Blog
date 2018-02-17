from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    """Definiuje niestandardowy menedżer do pobierania postów,
        których stan to 'published'."""
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()\
                                           .filter(status='published')
#Polega to na wywołaniu metody get_queryset() z filtrem obiektu models.Manager

class Post(models.Model):
    """Post tworzony przez użytkownika."""
    STATUS_CHOICES = (
                    ('draft', 'Roboczy'),
                    ('published', 'Opublikowany'),
                    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish',
                            )
    author = models.ForeignKey(User, related_name='blog_posts',
                               on_delete=models.CASCADE
                              )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
                              
    published = PublishedManager()
    objects = models.Manager()
    class Meta:
        ordering = ('-publish',)
        
    def __str__(self):
        """Zwraca reprezentację obiektu w postaci ciągu tekstowego(tytuł)."""
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                        args=[self.publish.year,
                              self.publish.strftime('%m'),
                              self.publish.strftime('%d'),
                              self.slug])

                                               
