from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'

class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug= models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=CASCADE) # (one_to_many) # If location is deleted, the whole event will be deleted with it
    participants = models.ManyToManyField(Participant, blank=True, null=True) # In many_to_many null doesn't really matter
    def __str__(self):
        return f'{self.title} - {self.slug}'