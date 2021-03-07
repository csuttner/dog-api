from dogs.models import Dog
from dogs.models import Breed
from dogs.serializers import DogSerializer
from dogs.serializers import BreedSerializer
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse

class DogDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Dog.objects.all()
  serializer_class = DogSerializer
  name = 'dog-detail'

class DogList(generics.ListCreateAPIView):
  queryset = Dog.objects.all()
  serializer_class = DogSerializer
  name = 'dog-list'

class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Breed.objects.all()
  serializer_class = BreedSerializer
  name = 'breed-detail'

class BreedList(generics.ListCreateAPIView):
  queryset = Breed.objects.all()
  serializer_class = BreedSerializer
  name = 'breed-list'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'dogs': reverse(DogList.name, request=request),
            'breeds': reverse(BreedList.name, request=request)
            })