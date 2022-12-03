from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Deck(models.Model):
    name = models.CharField(max_length=50)
    box_amount = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(6)]
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Box(models.Model):
    class Meta:
        verbose_name_plural = "boxes"

    number_of = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(6)]
    )
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    def __str__(self):
        return f"{str(self.number_of)}/{str(self.deck.box_amount)} ({self.deck.name})"


class Card(models.Model):
    front = models.CharField(max_length=150)
    back = models.CharField(max_length=150)
    active = models.BooleanField(default=True)
    delay = models.DateTimeField(blank=True, null=True)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)