from rest_framework import viewsets
from catalog.models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated

class GenreViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class PersonViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class StreamingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Streaming.objects.all()
    serializer_class = StreamingSerializer

class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer