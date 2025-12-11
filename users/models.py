from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    bio = models.TextField(blank=True)
    image = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    #followers: handled as a seperate relationship using follow model or ManyToMany
    followers = models.ManyToManyField('self',
                                       symmetrical=False,
                                       related_name='following',
                                       blank=True )
    def follower_count(self):
        return self.follower_count()
