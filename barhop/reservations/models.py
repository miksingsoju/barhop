from django.db import models

class Seating(models.Model):
    """A model that represents the Seating Entity."""

    name = models.CharField(max_length=255)
    capacity = models.IntegerField(default=1)
    desc = models.CharField(max_length=255)

    def __str__(self):
        """Returns the name of the model."""
        return self.name

    class Meta:
        """Metadata for the model."""
        verbose_name = 'Seating'


class Table(models.Model):
    """A model that represents the Table Entity."""

    seating = models.ForeignKey(Seating, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    desc = models.CharField(max_length=255)

    def __str__(self):
        """Returns the name of the model."""
        return self.seating

    class Meta:
        """Metadata for the model."""
        verbose_name = 'Table'
