
from django import forms
from .models import Review
# https://stackoverflow.com/questions/31691041/how-do-you-make-django-decimal-field-widgets-numberinput-increment-differently
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_description']
        widgets = {
            'review_description':forms.TextInput(attrs={'class': 'form-control'}),
            # 'review_rating': forms.NumberInput(attrs={'step': '0.5', 'min': '0', 'max': '5'}),
        }
    
