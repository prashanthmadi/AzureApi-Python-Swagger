from django.db import models

# Create your models here.
class Movie(models.Model):
    movieId = models.IntegerField()
    movieName = models.CharField(max_length=20)
    movieType = models.CharField(max_length=20)
    movieReleaseDate = models.DateTimeField()
    movieLength = models.IntegerField()

    class Meta:
        verbose_name_plural="Movies"