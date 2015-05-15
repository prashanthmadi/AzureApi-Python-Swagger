from rest_framework.response import Response
from rest_framework.views import APIView
from helloworld.models import Movie
from helloworld.serializers import MovieSerializer


class MovieList(APIView):
    def get(self,request,format=None):
        movies = Movie.objects.all()
        movies_serializer = MovieSerializer(movies,many=True)
        return Response(movies_serializer.data)

class MovieDetail(APIView):
    def get(self,request,pk,format=None):
        movie= Movie.objects.get(movieId=pk)
        movies_serializer=MovieSerializer(movie)
        return Response(movies_serializer.data)
