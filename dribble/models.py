from django.db import models

# Create your models here.
class Designer(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    def __str__(self):
        return self.username

class Post(models.Model):
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    caption = models.TextField(blank=True)
    category = models.CharField(max_length=255, default='')
    like = models.IntegerField(default=0)
    def __str__(self):
        return self.nama

class Response(models.Model):
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    date = models.DateField('date published')
    def __str__(self):
        return self.comment