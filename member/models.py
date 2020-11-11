from django.db import models
from cloudinary.models import CloudinaryField


class Member(models.Model):
    member_image = CloudinaryField('image')
    id_number = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    birth_day = models.DateField()
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.id_number



