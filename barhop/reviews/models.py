from django.db import models
from user_management.models import Profile
from bars.models import Bar, Amenity, BarImage
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal

# https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model
# https://www.geeksforgeeks.org/python/decimalfield-django-models/ 
# https://stackoverflow.com/questions/31691041/how-do-you-make-django-decimal-field-widgets-numberinput-increment-differently 

class Review(models.Model):
    review_user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    review_bar = models.ForeignKey(Bar, on_delete=models.CASCADE, null=True)
    review_description = models.TextField()
    review_date_created = models.DateTimeField(auto_now_add=True)
    review_rating = models.DecimalField(max_digits=2, decimal_places=1,
        validators=[
            MinValueValidator(Decimal('0.0')),
            MaxValueValidator(Decimal('5.0'))
        ])


    

    
    
    


