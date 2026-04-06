
from django import forms
from .models import Review
# https://stackoverflow.com/questions/31691041/how-do-you-make-django-decimal-field-widgets-numberinput-increment-differently
class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_description','review_rating']
        widgets = {
            'rating': forms.NumberInput(attrs={'step': '0.5', 'min': '0', 'max': '5'}),
        }
    
