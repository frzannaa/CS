from django.db import models


class Lecturer(models.Model):
 title = models.CharField(max_length=100)
 description = models.CharField(max_length=250)
 image = models.ImageField(upload_to='myapp/images/')
 url = models.URLField(blank=True)
 
# class Paper(models.Model):
#     title = models.CharField(max_length=255)
#     authors = models.CharField(max_length=255)
#     publication_date = models.DateField()
#     doi = models.CharField(max_length=255)
#     source = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='movie/images/')
    
#     def __str__(self):
#         return self.title