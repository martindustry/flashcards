from django.db import models
from users.models import User


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
    public = models.BooleanField(default=False)
    randomized = models.BooleanField(default=False)
    reversed = models.BooleanField(default=False)

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

    def get_time(self):
        return self.timestamp.strftime('%b %d %Y, %I:%M %p')
