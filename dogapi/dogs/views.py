from dogs.models import Dog
from dogs.models import Breed
from dogs.serializers import DogSerializer
from dogs.serializers import BreedSerializer
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

class DogList(generics.ListCreateAPIView):
  queryset = Dog.objects.all()
  serializer_class = DogSerializer

class DogDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Dog.objects.all()
  serializer_class = DogSerializer

class BreedList(generics.ListCreateAPIView):
  queryset = Breed.objects.all()
  serializer_class = BreedSerializer

class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Breed.objects.all()
  serializer_class = BreedSerializer



