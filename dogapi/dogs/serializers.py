from rest_framework import serializers
from dogs.models import Dog
from dogs.models import Breed

class DogSerializer(serializers.HyperlinkedModelSerializer):
  breed = serializers.SlugRelatedField(queryset=Breed.objects.all(), slug_field='name')
  gender = serializers.ChoiceField(choices=Dog.GENDER_CHOICES)
  gender_description = serializers.CharField(source='get_gender_display', read_only=True)

  class Meta:
    model = Dog
    
    fields = (
      'url',
      'breed',
      'name',
      'age',
      'gender',
      'gender_description',
      'color',
      'favoritefood',
      'favoritetoy',
    )

class BreedSerializer(serializers.HyperlinkedModelSerializer):
  dogs = DogSerializer(many=True, read_only=True)
  size = serializers.ChoiceField(choices=Breed.SIZE_CHOICES)
  size_description = serializers.CharField(source='get_size_display', read_only=True)

  class Meta:
    model = Breed

    fields = (
      'url',
      'name',
      'size',
      'size_description',
      'friendliness',
      'trainability',
      'sheddingamount',
      'exerciseneeds',
      'dogs',
    )