from django.db import models

class Categories(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'

class Post(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=20)
    content = models.TextField()
    catogories = models.CharField(
        max_length = 2,
        choices = Categories.choices,
        default = Categories.GR,
    )

    approved = models.BooleanField(default = True)

    def __str__(self):
        return self.title