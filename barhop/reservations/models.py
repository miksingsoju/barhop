from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    class UserType(models.TextChoices):
        BAR_OWNER = "OWNER", "Bar Owner"
        BARHOPPER = "HOPPER", "Barhopper"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    email = models.EmailField(unique=True)

    user_type = models.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.BARHOPPER
    )

    def __str__(self):
        return self.user.username
