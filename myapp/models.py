from django.db import models

# Create your models here.

class Music(models.Model):

     class Meta:
          db_table = 'music'
     id = models.AutoField(primary_key=True)
     title = models.CharField(max_length=200)
     seconds = models.IntegerField()

     def __str__(self):
          return str(self.title)