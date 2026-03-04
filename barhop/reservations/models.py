from django.db import models
from user_management.models import Profile
from bars.models import Bar


def upload_path_handler(instance, filename):
    return "bars/{id}/seats/{file}".format(id=instance.bar.id, file=filename)


class Table(models.Model):
    """A model that represents the Table Entity."""

    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
    table_type = models.CharField(max_length=255)
    qty = models.IntegerField(default=1)
    capacity = models.IntegerField(default=1)
    image = models.ImageField(upload_to=upload_path_handler, null=True, blank=True)

    def __str__(self):
        """Returns the name of the model."""
        return self.table_type

    class Meta:
        """Metadata for the model."""
        verbose_name = 'Table'


class Reservation(models.Model):
    """A model that represents the Reservation Entity."""

    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    hopper = models.ForeignKey(Profile, on_delete=models.CASCADE)
    guests = models.IntegerField(default=0)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    # status = 


    def __str__(self):
        """Returns the name of the model."""
        return f"{self.table_type} for {self.hopper.first_name}"

    class Meta:
        """Metadata for the model."""
        verbose_name = 'Reservation'
