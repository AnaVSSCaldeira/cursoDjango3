from django.db import models

class Categories(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

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
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_category_label(self):
        return self.get_catogories_display()