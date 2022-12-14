from django.db import models
from users.models import User
from flashcards import LANG_CHOICES


class Collection(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='collections'
    )
    followers = models.ManyToManyField(
        User,
        related_name='following',
        blank=True
    )
    language1 = models.CharField(max_length=50, choices=LANG_CHOICES)
    language2 = models.CharField(max_length=50, choices=LANG_CHOICES)
    public = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.id})"


class Flashcard(models.Model):
    task = models.CharField(max_length=250)
    solution = models.CharField(max_length=250)
    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        related_name='flashcards',
    )

    def __str__(self):
        return f"#{self.id}"


class Log(models.Model):
    visitor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='visited_collections'
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        related_name='visits'
    )
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.visitor.username} - {self.collection.title}"


class Setting(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='setting'
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        related_name='setting'
    )
    index = models.IntegerField(default=0)
    random = models.BooleanField(default=False)
    reversed = models.BooleanField(default=False)
    order = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Settings on Collection {self.collection.id}"

    def serialize(self):
        return {
            'index': self.index,
            'random': self.random,
            'reversed': self.reversed,
            'order': self.order
        }
