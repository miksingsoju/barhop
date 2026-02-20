from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    class UserType(models.TextChoices):
        BAR_OWNER = "OWNER", "Bar Owner"
        BARHOPPER = "HOPPER", "Bar Hopper"

    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_of_birth = models.DateField(null=True, blank=True)

    user_type = models.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.BARHOPPER
    )

    def __str__(self):
        return self.username