from django.db import models

# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length =100)
    content = models.TextField()
    poster = models.CharField(max_length=100)

    #uproad image path save place
    sns_image = models.ImageField(upload_to='')
    good = models.IntegerField(null=True, blank=True, default=1)
    read = models.IntegerField(null=True, blank=True, default=1)
    read_text = models.TextField(null=True, blank=True, default='test_admin')

