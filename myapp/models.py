from django.db import models

# Create your models here.

class Music(models.Model):

     class Meta:
          db_table = 'music'

     cover = models.FileField()
     title = models.CharField(max_length=200)
     seconds = models.IntegerField()

     def __str__(self):
          return str(self.title)