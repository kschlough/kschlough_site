from django.db import models

class BlogPost(models.Model):
    # id - Django automatically creates an auto-incrementing primary key  
    # for every model
    title = models.CharField(max_length=120, null=True, blank=False)
    subtitle = models.CharField(max_length=180, null=True, blank=False)
    slug = models.CharField(max_length=240, null=True, blank=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
