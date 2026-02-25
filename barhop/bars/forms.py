from django import forms
from .models import Bar 
# will fix in the future

class CreateBarForm(forms.ModelForm):
    class Meta: 
        model = Bar
        fields = ['bar_name', 'bar_description', 'bar_start_time', 'bar_end_time', 'bar_amenities']
        widgets = {
            'bar_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bar_description':forms.TextInput(attrs={'class': 'form-control'}),
            'bar_start_time': forms.TimeInput(format='%H:%M',attrs={'type': 'time', 'class': 'form-control'}),
            'bar_end_time': forms.TimeInput(format='%H:%M',attrs={'type': 'time', 'class': 'form-control'}),
            'bar_amenities': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'bar_name': 'Name of bar',
            'bar_description': 'Bar description',
            'bar_start_time': 'Opening time',
            'bar_end_time': 'Closing time',
            'bar_amenities': 'Select amenities',
        }
        def clean(self):
            if self.bar_start_time is not None and self.bar_end_time is not None:
                if self.start_time > self.end_time:
                    raise ValidationError("You can't end a bar before it started. How are we supposed to bar hop now...")



 


