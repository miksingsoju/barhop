from django.db import models
from user_management.models import Profile
from bars.models import Bar


def upload_path_handler(instance, filename):
    return "bars/{id}/seats/{file}".format(id=instance.bar.id, file=filename)


class Seating(models.Model):
    """A model that represents the Seating Entity."""

    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
    seating = models.CharField(max_length=255)
    capacity = models.IntegerField(default=1)
    image = models.ImageField(upload_to=upload_path_handler, null=True, blank=True)

    def __str__(self):
        """Returns the name of the model."""
        return self.seating

    class Meta:
        """Metadata for the model."""
        verbose_name = 'Seating'


class Table(models.Model):
    """A model that represents the Table Entity."""

    table_type = models.ForeignKey(Seating, on_delete=models.CASCADE)

    def __str__(self):
        """Returns the name of the model."""
        return str(self.table_type)

    class Meta:
        """Metadata for the model."""
        verbose_name = 'Table'


class Reservation(models.Model):
    """A model that represents the Reservation Entity."""

    tables = models.ManyToManyField(Table)
    hopper = models.ForeignKey(Profile, on_delete=models.CASCADE)
    guests = models.IntegerField(default=0)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    
    STATUS_CHOICES = [
        ('CONFIRMED', 'Confirmed'),
        ('PENDING', 'Pending'),
        ('REJECTED', 'Rejected'),
        ('CANCELLED', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')


    def __str__(self):
        """Returns the name of the model."""
        return f"{self.hopper.first_name} at {self.date}, {self.start_time} - {self.end_time}"

    class Meta:
        """Metadata for the model."""
        verbose_name = 'Reservation'
