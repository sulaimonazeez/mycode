from django.db import models

class musicUploader(models.Model):
  title = models.CharField(max_length=255)
  image = models.ImageField(upload_to='myapp/static')
  music = models.FileField(upload_to='myapp/static')
  def __str__(self):
    return self.title