from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=25, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='tag of username')
        ]

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    fullname = models.CharField(null=False)
    born_date = models.CharField(null=False)
    born_location = models.CharField(null=False)
    description = models.CharField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.fullname}"


class Note(models.Model):
    quote = models.CharField(max_length=150, null=False)
    tags = models.CharField(max_length=150, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.quote}"
