from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

class PostComment(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='comments')

    def __str__(self):
        return self.message
