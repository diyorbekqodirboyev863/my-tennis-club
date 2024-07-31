from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, blank=True)
    joined_date = models.DateField(null=True)
    slug = models.SlugField(default="", null=False)
    bio = models.TextField(max_length=500, null=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
