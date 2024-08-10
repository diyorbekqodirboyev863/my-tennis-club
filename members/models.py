from django.db import models
from django.utils.text import slugify

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, blank=True)
    joined_date = models.DateField(null=True)
    slug = models.SlugField(default="", null=False)
    bio = models.TextField(max_length=500, blank=True, null=True)
    profile_image = models.ImageField(upload_to='members/', blank=True, null=True) # New.
    phone_number = models.CharField(max_length=50, blank=True, null=True) # New.

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.firstname} {self.lastname}')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
