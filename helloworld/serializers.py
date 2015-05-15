from rest_framework import serializers
from helloworld.models import Movie

__author__ = 'prashanth'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields=('movieId','movieName','movieType','movieReleaseDate','movieLength')