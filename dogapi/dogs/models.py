from django.db import models

class Dog(models.model):
  name = models.CharField(max_length=200, default='', blank=False)
  age = models.IntegerField()
  breed = models.ForeignKey(
    Breed,
    on_delete=models.CASCADE,
  )

  MALE = 'M'
  FEMALE = 'F'
  GENDER_CHOICES = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
  )

  gender = models.CharField(
    max_length=2,
    choices=GENDER_CHOICES,
    default=MALE,
    blank=False
  )
  color = models.CharField(max_length=50, default='', blank=False)
  favoritefood = models.CharField(max_length=200, default='', blank=False)
  favoritetoy = models.CharField(max_length=200, default='', blank=False)

  class Meta:
    ordering = ('name',) 

  def __str__(self):
    return self.name

class Breed(models.model):
  name = models.CharField(max_length=200, default='', blank=False)

  TINY = 'T'
  SMALL = 'S'
  MEDIUM = 'M'
  LARGE = 'L'

  SIZE_CHOICES = (
    (TINY, 'Tiny'),
    (SMALL, 'Small'),
    (MEDIUM, 'Medium'),
    (LARGE, 'Large')
  )

  size = models.CharField(
    max_length=2,
    choices=SIZE_CHOICES,
    default=MEDIUM,
    blank=False
  )

  VALUE_CHOICES = (1, 2, 3, 4, 5)

  friendliness = models.IntegerField(choices=VALUE_CHOICES, default=3, blank=False)
  trainability = models.IntegerField(choices=VALUE_CHOICES, default=3, blank=False)
  sheddingamount = models.IntegerField(choices=VALUE_CHOICES, default=3, blank=False)
  exerciseneeds = models.IntegerField(choices=VALUE_CHOICES, default=3, blank=False)

  class Meta:
    ordering = ('name',) 

  def __str__(self):
    return self.name