from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_email, validate_password_strength, validate_username, validate_email, validate_date_of_birth

class Profile(AbstractUser):
    class UserType(models.TextChoices):
        BAR_OWNER = "OWNER", "Bar Owner"
        BARHOPPER = "HOPPER", "Bar Hopper"

    username = models.CharField(max_length=150, unique=True, validators=[validate_username])
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    email = models.EmailField(unique=True, validators=[validate_email])
    password = models.CharField(max_length=128, validators=[validate_password_strength])
    date_of_birth = models.DateField(null=True, blank=True, validators=[validate_date_of_birth])
    bio = models.TextField(max_length=500, blank=True, default="No bio yet.")

    user_type = models.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.BARHOPPER
    )

    def __str__(self):
        return self.username