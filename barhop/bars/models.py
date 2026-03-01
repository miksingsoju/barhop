from django.db import models
from user_management.models import Profile

# class City(models.Model): 
#     name = models.CharField(max_length=200)

# class Barangay(models.Model):
#     city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="barangays")
#     name = models.CharField(max_length=200)

#     class Meta:
#         unique_together = {'city', 'name'}

# class Address(models.Model):
#     city = models.ForeignKey(City, on_delete=models.PROTECT)
#     barangay = models.ForeignKey(Barangay, on_delete=models.PROTECT)
#     street = models.CharField(max_length=200)

class Amenity(models.Model):
    name = models.CharField(max_length=67)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Amenity'
        verbose_name_plural = 'Amenities'

class Bar(models.Model):
    bar_draft = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    bar_name = models.CharField(max_length=67)
    bar_description = models.TextField()
    bar_owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    bar_address = models.TextField(default="Metro Manila")
    # address = models.OneToOneField(Address, on_delete=models.CASCADE)
    bar_amenities = models.ManyToManyField(Amenity, blank=True)
    STATUS_CHOICES = [
        ('FIRE', 'On fire!'),
        ('LUKEWARM', 'Warming up'),
        ('COLD', 'Cold case'),
    ]
    # Note: these are just placeholder statuses 
    bar_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='COLD')
    bar_start_time = models.TimeField()
    bar_end_time = models.TimeField()
    
    def __str__(self):
        return self.bar_name
     
    class Meta:
        verbose_name = 'Bar'
        verbose_name_plural = 'Bars'


class BarImage(models.Model):
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='bar_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Bar Image'
        verbose_name_plural = 'Bar Images'

    def __str__(self):
        return f"Image for {self.bar.bar_name}"

