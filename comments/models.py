from django.db import models
from django.conf import settings
from articles.models import Article

# Create your models here.
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name="comments") 
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

