from django import forms
from .models import Bar, Amenity
from django.core.exceptions import ValidationError
# will fix in the future

class CreateBarForm(forms.ModelForm):
    class Meta: 
        model = Bar
        fields = ['bar_name', 'bar_description', 'bar_start_time', 'bar_end_time', 'bar_address', 'bar_amenities']
        widgets = {
            'bar_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bar_description':forms.TextInput(attrs={'class': 'form-control'}),
            'bar_start_time': forms.TimeInput(format='%H:%M',attrs={'type': 'time', 'class': 'form-control'}),
            'bar_end_time': forms.TimeInput(format='%H:%M',attrs={'type': 'time', 'class': 'form-control'}),
            'bar_address':forms.TextInput(attrs={'class': 'form-control'}),
            'bar_amenities': forms.SelectMultiple(),
        }
    def clean_bar_end_time(self):
        bar_start_time = self.cleaned_data.get('bar_start_time')
        bar_end_time = self.cleaned_data.get('bar_end_time')

        if bar_start_time and bar_end_time and bar_start_time > bar_end_time:
            raise ValidationError("You can't end a bar before it started. How are we supposed to bar hop now...")

        return bar_end_time
