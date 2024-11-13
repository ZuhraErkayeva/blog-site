from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )
    profile_image = models.ImageField(
        upload_to='profile_images/',
        default='profile_images/default.jpg',
        blank=True
    )
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s profile"

class UserToken(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='token')
    token = models.UUIDField(default=uuid.uuid4(), editable=False, unique=True)

    def __str__(self):
        return f"{self.user.user.username}{self.token}"




