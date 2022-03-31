from django.db import models

# Create your models here.
class Post(models.Model): # 상속
    title = models.CharField(max_length=30)
    content = models.TextField()
    create_at = models.DateTimeField()