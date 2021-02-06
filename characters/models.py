from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    player = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    species = models.CharField(max_length=100)
    gravity = models.CharField(max_length=10)
    sex = models.CharField(max_length=2)
    heignt = models.DecimalField(default=1.75, max_digits=4, decimal_places=2)
    weight = models.IntegerField(default=75)
    planet = models.CharField(max_length=80)
    schooling = models.CharField(max_length=20)
    occupation = models.CharField(max_length=22)
    age = models.IntegerField(default=21)
    wealth = models.IntegerField(default=20)
    strength = models.IntegerField(default=2)
    reflex= models.IntegerField(default=2)
    health = models.IntegerField(default=2)
    intuition = models.IntegerField(default=2)
    will = models.IntegerField(default=2)
    presence = models.IntegerField(default=2)

    def __str__(self):
        return self.name
