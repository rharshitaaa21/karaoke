from django.db import models

class Artist(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    language = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
    

class Album(models.Model):
    title  = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    is_favourite = models.BooleanField(default=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}{self.artist}{self.is_favourite}"
