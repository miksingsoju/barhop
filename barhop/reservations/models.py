from django.db import models
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
