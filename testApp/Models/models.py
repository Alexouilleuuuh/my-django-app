from django.db import models

# Create your models here.

class DataFile(models.Model):
    name = models.CharField(max_length=100)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    content = models.FileField(upload_to='data_files')
