from django.db import models

class Free(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    avi_date = models.CharField(blank=True, max_length=20)
    price = models.CharField(blank=True, max_length=10)
    img = models.ImageField(blank=True, upload_to='image')

    def __str__(self):
        return self.title

class Half(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    avi_date = models.CharField(blank=True, max_length=20)
    price = models.CharField(blank=True, max_length=10)
    img = models.ImageField(blank=True, upload_to='image')

    def __str__(self):
        return self.title
