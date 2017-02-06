from django.db import models

class Post(models.Model):
    image = models.ImageField()
    filtered_image = models.ImageField()
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
