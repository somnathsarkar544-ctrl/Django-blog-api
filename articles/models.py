from django.db import models
from django.conf import settings
from django.utils.text import slugify
from slugify import slugify as pyslug

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50,unique=True) # tag name should be unique

    def __str__(self):
        return self.name # return the tag name as string representation


class Article (models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="articles") 
    title = models.CharField(max_length=300) # title of the article
    body = models.TextField() # main content of the article
    slug = models.SlugField(max_length=300,unique=True,blank=True) # slug field to create url friendly representation of the title
    tags = models.ManyToManyField(Tag,blank=True,related_name='articles') # many to many relationship with tag model
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="liked_articles",blank=True) # users who liked the article
    created_at = models.DateTimeField(auto_now_add=True) # timestamp when the article is created
    updated_at = models.DateTimeField(auto_now=True) # timestamp when the article is last updated


    class Meta:
        ordering = ['-created_at']
    
    def save(self, *args,**kwargs):
        if not self.slug:
            base = pyslug(self.title)[:200]
            slug= base
            i = 1
            while Article.objects.filter(slug=slug).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    def favorites_count(self):
        return self.likes.count() # return the number of likes for the article

