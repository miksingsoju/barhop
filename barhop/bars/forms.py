from django import forms
from django.core.exceptions import ValidationError
from .models import Bar


class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultiImageField(forms.ImageField):

    widget = MultiFileInput

    def clean(self, data, initial=None):
        if data in self.empty_values:
            if self.required and not initial:
                raise ValidationError(self.error_messages["required"], code="required")
            return []

        if not isinstance(data, (list, tuple)):
            data = [data]
        cleaned_files = []
        for f in data:
            cleaned_files.append(super().clean(f, initial))
        return cleaned_files


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
            'bar_amenities': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'bar_name': 'Name of bar',
            'bar_description': 'Bar description',
            'bar_start_time': 'Opening time',
            'bar_end_time': 'Closing time',
            'bar_address' : 'Bar Address', 
            'bar_amenities': 'Select amenities',
        }

    images = MultiImageField(label='Add bar images: (optional)', required=False)

    def clean_bar_end_time(self):
        bar_start_time = self.cleaned_data.get('bar_start_time')
        bar_end_time = self.cleaned_data.get('bar_end_time')

        if bar_start_time and bar_end_time and bar_start_time > bar_end_time:
            raise ValidationError("You can't end a bar before it started. How are we supposed to bar hop now...")

        return bar_end_time
