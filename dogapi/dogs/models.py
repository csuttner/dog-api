from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Breed(models.Model):
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

  friendliness = models.IntegerField(
    default=3,
    validators=[MaxValueValidator(5), MinValueValidator(1)]
  )
  trainability = models.IntegerField(
    default=3,
    validators=[MaxValueValidator(5), MinValueValidator(1)]
  )
  sheddingamount = models.IntegerField(
    default=3,
    validators=[MaxValueValidator(5), MinValueValidator(1)]
  )
  exerciseneeds = models.IntegerField(
    default=3,
    validators=[MaxValueValidator(5), MinValueValidator(1)]
  )

  class Meta:
    ordering = ('name',) 

  def __str__(self):
    return self.name

class Dog(models.Model):
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